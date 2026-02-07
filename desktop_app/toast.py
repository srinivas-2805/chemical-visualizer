from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer


class Toast(QWidget):
    def __init__(self, message, success=True, parent=None):
        super().__init__(parent)

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Tool |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        bg_color = "#2ecc71" if success else "#e74c3c"

        self.label = QLabel(message)
        self.label.setStyleSheet(f"""
            QLabel {{
                background: {bg_color};
                color: white;
                padding: 12px 18px;
                border-radius: 10px;
                font-weight: 600;
            }}
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        QTimer.singleShot(3000, self.close)

    def show_top_right(self):
        screen = self.screen().availableGeometry()
        self.adjustSize()

        x = screen.right() - self.width() - 20
        y = screen.top() + 20

        self.move(x, y)
        self.show()
