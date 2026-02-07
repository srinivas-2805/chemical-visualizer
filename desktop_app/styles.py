

LIGHT_STYLE = """
QWidget {
    background-color: #f2f4f8;
    color: #222;
    font-family: Segoe UI;
    font-size: 14px;
}

QFrame {
    background: white;
    border-radius: 14px;
}

QLineEdit {
    background: white;
    color: #222;
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #ccc;
}

QPushButton {
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #667eea,
        stop:1 #764ba2
    );
    color: white;
    padding: 10px;
    border-radius: 10px;
    font-weight: 600;
}
"""

DARK_STYLE = """
QWidget {
    background-color: #121212;
    color: #eaeaea;
    font-family: Segoe UI;
    font-size: 14px;
}

QFrame {
    background: #1e1e1e;
    border-radius: 14px;
}

QLineEdit {
    background: #1e1e1e;
    color: #eaeaea;
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #444;
}

QPushButton {
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #43cea2,
        stop:1 #185a9d
    );
    color: white;
    padding: 10px;
    border-radius: 10px;
    font-weight: 600;
}
"""


LIGHT_LIST_STYLE = """
QListWidget {
    background: #ffffff;
    border-radius: 10px;
    padding: 6px;
}

QListWidget::item {
    padding: 10px;
    border-radius: 6px;
    color: #222;
}

QListWidget::item:selected {
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #667eea,
        stop:1 #764ba2
    );
    color: white;
}
"""

DARK_LIST_STYLE = """
QListWidget {
    background: #1e1e1e;
    border-radius: 10px;
    padding: 6px;
}

QListWidget::item {
    padding: 10px;
    border-radius: 6px;
    color: #eaeaea;
}

QListWidget::item:selected {
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #667eea,
        stop:1 #764ba2
    );
    color: white;
}
"""

