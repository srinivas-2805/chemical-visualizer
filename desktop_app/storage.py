import json
import os

# =========================
# FILE PATHS
# =========================

TOKEN_PATH = os.path.expanduser("~/.chemical_visualizer_token.json")
THEME_PATH = os.path.expanduser("~/.chemical_visualizer_theme.json")


# =========================
# TOKEN STORAGE
# =========================

def save_token(token):
    with open(TOKEN_PATH, "w") as f:
        json.dump({"token": token}, f)


def load_token():
    if not os.path.exists(TOKEN_PATH):
        return None
    try:
        with open(TOKEN_PATH, "r") as f:
            return json.load(f).get("token")
    except Exception:
        return None


def clear_token():
    if os.path.exists(TOKEN_PATH):
        os.remove(TOKEN_PATH)


# =========================
# THEME STORAGE  ✅ ADDED
# =========================

def save_theme(theme):
    """
    theme: 'light' or 'dark'
    """
    with open(THEME_PATH, "w") as f:
        json.dump({"theme": theme}, f)


def load_theme():
    if not os.path.exists(THEME_PATH):
        return "light"   # default theme
    try:
        with open(THEME_PATH, "r") as f:
            return json.load(f).get("theme", "light")
    except Exception:
        return "light"
