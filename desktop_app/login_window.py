from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox, QFrame
)
from PyQt5.QtCore import Qt
import api


class LoginWindow(QWidget):
    def __init__(self, on_success):
        super().__init__()
        self.on_success = on_success
        self.is_logging_in = False

        self.setWindowTitle("Login")
        self.setFixedSize(360, 280)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("🔐 Login")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size:22px; font-weight:600;")

        card = QFrame()
        card_layout = QVBoxLayout(card)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self.handle_login)

        card_layout.addWidget(self.username_input)
        card_layout.addWidget(self.password_input)
        card_layout.addWidget(self.login_btn)

        layout.addWidget(title)
        layout.addWidget(card)
        self.setLayout(layout)

    def handle_login(self):
        if self.is_logging_in:
            return

        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Username and password required")
            return

        self.is_logging_in = True
        self.login_btn.setEnabled(False)

        # 🔐 AUTH ONLY
        try:
            api.login(username, password)
        except Exception:
            QMessageBox.critical(self, "Login Failed", "Invalid credentials")
            self.is_logging_in = False
            self.login_btn.setEnabled(True)
            return

        # 🖥️ UI SUCCESS
        try:
            self.on_success()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "App Error", str(e))

        self.is_logging_in = False
        self.login_btn.setEnabled(True)
