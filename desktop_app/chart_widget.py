from PyQt5.QtWidgets import QWidget, QVBoxLayout, QToolTip
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class BarChart(QWidget):
    def __init__(self):
        super().__init__()

        self.figure = Figure(facecolor="#1e1e1e")
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

        self.ax = self.figure.add_subplot(111)
        self.bars = []
        self.labels = []
        self.values = []

        self.canvas.setMouseTracking(True)
        self.canvas.mpl_connect("motion_notify_event", self.on_hover)

    def update_chart(self, type_distribution: dict):
        self.ax.clear()

        self.labels = list(type_distribution.keys())
        self.values = list(type_distribution.values())

        colors = ["#b388ff", "#00e5c0", "#ff5252", "#ffd166", "#4dd0e1"]

        self.bars = self.ax.bar(
            self.labels,
            self.values,
            color=colors[: len(self.labels)]
        )

        self.ax.set_title("Equipment Distribution", color="white")
        self.ax.set_ylabel("Count", color="white")
        self.ax.tick_params(colors="white")
        self.ax.set_facecolor("#1e1e1e")

        self.figure.tight_layout()
        self.canvas.draw()

    def on_hover(self, event):
        if event.inaxes != self.ax:
            QToolTip.hideText()
            return

        for bar, label, value in zip(self.bars, self.labels, self.values):
            contains, _ = bar.contains(event)
            if contains:
                QToolTip.showText(
                    QCursor.pos(),
                    f"<b>{label}</b><br/>Equipment Count: {value}",
                )
                return

        QToolTip.hideText()
