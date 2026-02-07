import sys
from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow
from dashboard_window import Dashboard
from styles import LIGHT_STYLE, DARK_STYLE
from storage import load_theme
import api

app = QApplication(sys.argv)

theme = load_theme()
app.setStyleSheet(DARK_STYLE if theme == "dark" else LIGHT_STYLE)

dashboard = None
login = None


def open_dashboard():
    global dashboard, login
    if login:
        login.close()
        login = None
    dashboard = Dashboard(on_logout=open_login)
    dashboard.show()


def open_login():
    global login, dashboard
    if dashboard:
        dashboard.close()
        dashboard = None
    login = LoginWindow(open_dashboard)
    login.show()



if api.load_token():        
    open_dashboard()
else:
    open_login()

sys.exit(app.exec_())
