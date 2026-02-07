from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QListWidget, QPushButton,
    QFileDialog, QHBoxLayout,
    QLineEdit, QApplication,
    QGridLayout, QGroupBox, QMessageBox
)
from PyQt5.QtCore import Qt,QTimer

import api
from toast import Toast
from chart_widget import BarChart
from storage import save_theme, load_theme
from styles import (
    LIGHT_STYLE, DARK_STYLE,
    LIGHT_LIST_STYLE, DARK_LIST_STYLE
)


class Dashboard(QWidget):
    def __init__(self, on_logout):
        super().__init__()
        self.on_logout = on_logout
        self.datasets = []
        self.filtered = []
        self.is_busy = False

        self.setWindowTitle("Dashboard")
        self.setMinimumSize(760, 620)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(10)

        # ================= HEADER =================
        header = QLabel("📊 Upload History")
        header.setStyleSheet("font-size:20px; font-weight:600;")

        btn_layout = QHBoxLayout()

        self.upload_btn = QPushButton("Upload CSV")
        self.upload_btn.clicked.connect(self.choose_csv)

        self.download_btn = QPushButton("Download PDF")
        self.download_btn.clicked.connect(self.download_pdf)

        self.theme_btn = QPushButton()
        self.update_theme_icon()
        self.theme_btn.clicked.connect(self.toggle_theme)

        logout_btn = QPushButton("Logout")
        logout_btn.setStyleSheet("background:#ff4b2b;")
        logout_btn.clicked.connect(self.handle_logout)

        btn_layout.addWidget(self.upload_btn)
        btn_layout.addWidget(self.download_btn)
        btn_layout.addWidget(self.theme_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(logout_btn)

        divider = QLabel()
        divider.setFixedHeight(1)
        divider.setStyleSheet("background:#555; margin:6px 0;")

        # ================= FILE LABEL =================
        self.selected_file_label = QLabel("No file selected")
        self.selected_file_label.setStyleSheet("color:#888; margin:4px;")

        # ================= SEARCH =================
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search datasets...")
        self.search_input.textChanged.connect(self.apply_filter)

        # ================= SUMMARY =================
        self.summary_box = QGroupBox("📈 Dataset Summary")
        self.summary_box.hide()

        grid = QGridLayout()
        self.total_label = QLabel("-")
        self.flow_label = QLabel("-")
        self.pressure_label = QLabel("-")
        self.temp_label = QLabel("-")
        self.type_label = QLabel("-")

        fields = [
            ("Total Count", self.total_label),
            ("Avg Flowrate", self.flow_label),
            ("Avg Pressure", self.pressure_label),
            ("Avg Temperature", self.temp_label),
            ("Type Distribution", self.type_label),
        ]

        for r, (t, v) in enumerate(fields):
            title = QLabel(t)
            title.setStyleSheet("font-weight:600;")
            grid.addWidget(title, r, 0)
            grid.addWidget(v, r, 1)

        self.summary_box.setLayout(grid)

        # ================= CHART =================
        self.chart = BarChart()
        self.chart.hide()

        # ================= LIST =================
        self.list_widget = QListWidget()
        self.list_widget.currentRowChanged.connect(self.update_summary)
        self.apply_list_theme()

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color:#888;")

        # ================= LAYOUT ORDER =================
        main_layout.addWidget(header)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(divider)
        main_layout.addWidget(self.selected_file_label)
        main_layout.addWidget(self.search_input)
        main_layout.addWidget(self.summary_box)
        main_layout.addWidget(self.chart)
        main_layout.addWidget(self.list_widget)
        main_layout.addWidget(self.status_label)

        self.load_history()
        # 🔁 AUTO REFRESH TIMER
        self.refresh_timer = QTimer(self)
        self.refresh_timer.timeout.connect(self.auto_refresh)
        self.refresh_timer.start(5000)  # 5 seconds


    # ================= THEME =================
    def update_theme_icon(self):
        self.theme_btn.setText("☀️ Light" if load_theme() == "dark" else "🌙 Dark")

    def toggle_theme(self):
        app = QApplication.instance()
        new_theme = "dark" if load_theme() == "light" else "light"
        save_theme(new_theme)
        app.setStyleSheet(DARK_STYLE if new_theme == "dark" else LIGHT_STYLE)
        self.update_theme_icon()
        self.apply_list_theme()
        self.chart.update_chart({})  # refresh colors safely

    def apply_list_theme(self):
        self.list_widget.setStyleSheet(
            DARK_LIST_STYLE if load_theme() == "dark" else LIGHT_LIST_STYLE
        )

    # ================= DATA =================
    def load_history(self, auto_select_latest=False):
        self.datasets = api.get_history()
        self.filtered = self.datasets.copy()
        self.render_list()
        self.clear_summary()

        if auto_select_latest and self.filtered:
            self.list_widget.setCurrentRow(0)

    def render_list(self):
        self.list_widget.clear()
        if not self.filtered:
            self.list_widget.addItem("No datasets found")
            return

        for i, d in enumerate(self.filtered, 1):
            self.list_widget.addItem(f"#{i}  {d['name']}")

    def apply_filter(self, text):
        text = text.lower()
        self.filtered = [d for d in self.datasets if text in d["name"].lower()]
        self.render_list()
        self.clear_summary()

    # ================= SUMMARY =================
    def clear_summary(self):
        for lbl in (
            self.total_label, self.flow_label,
            self.pressure_label, self.temp_label,
            self.type_label
        ):
            lbl.setText("-")
        self.summary_box.hide()
        self.chart.hide()

    def update_summary(self, index):
        if index < 0 or index >= len(self.filtered):
            self.clear_summary()
            return

        summary = self.filtered[index].get("summary")
        if not summary:
            self.clear_summary()
            return

        self.summary_box.show()

        def fmt(v):
            if v is None:
                return "-"
            if isinstance(v, float):
                return f"{v:.2f}"
            return str(v)

        self.total_label.setText(fmt(summary.get("total_count")))
        self.flow_label.setText(fmt(summary.get("average_flowrate")))
        self.pressure_label.setText(fmt(summary.get("average_pressure")))
        self.temp_label.setText(fmt(summary.get("average_temperature")))


        type_dist = summary.get("type_distribution", {})
        self.type_label.setText(
            ", ".join(f"{k}: {v}" for k, v in type_dist.items())
        )

        if type_dist:
            self.chart.show()
            self.chart.update_chart(type_dist)
        else:
            self.chart.hide()
       


    # ================= CSV =================
    def choose_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV", "", "CSV Files (*.csv)"
        )
        if not file_path:
            return

        self.selected_file_label.setText(f"📄 Selected: {file_path.split('/')[-1]}")

        try:
            api.upload_csv(file_path)
            Toast("CSV uploaded successfully", True, self).show_top_right()
            self.load_history(auto_select_latest=True)
        except Exception as e:
            QMessageBox.critical(self, "Upload Failed", str(e))

    # ================= PDF =================
    def download_pdf(self):
        index = self.list_widget.currentRow()
        if index < 0:
            Toast("Select a dataset first", False, self).show_top_right()
            return

        dataset = self.filtered[index]
        path, _ = QFileDialog.getSaveFileName(
            self, "Save PDF", f"{dataset['name']}_report.pdf", "PDF Files (*.pdf)"
        )

        if not path:
            return

        try:
            api.download_pdf(dataset["id"], path)
            Toast("PDF downloaded", True, self).show_top_right()
        except Exception as e:
            Toast(str(e), False, self).show_top_right()
    

    def auto_refresh(self):
        if self.is_busy:
            return

        try:
            latest = api.get_history()
        except Exception:
            return  # backend unreachable → ignore silently
        if not latest:
            return

        # Detect change (new dataset uploaded)
        if not self.datasets or latest[0]["id"] != self.datasets[0]["id"]:
            self.datasets = latest
            self.filtered = latest.copy()
            self.render_list()

            # Auto-select latest dataset
            self.list_widget.setCurrentRow(0)
            Toast("🔄 New dataset detected", True, self).show_top_right()


    # ================= LOGOUT =================
    def handle_logout(self):
        self.refresh_timer.stop()
        api.logout()
        self.close()
        self.on_logout()
