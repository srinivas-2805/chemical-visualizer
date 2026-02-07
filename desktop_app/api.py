import requests
import os

BASE_URL = "http://127.0.0.1:8000/api"
TOKEN_FILE = "token.txt"


def save_token(token):
    with open(TOKEN_FILE, "w") as f:
        f.write(token)


def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE) as f:
            return f.read().strip()
    return None


def clear_token():
    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)


def headers():
    token = load_token()
    if not token:
        raise Exception("Not authenticated")
    return {"Authorization": f"Token {token}"}


def login(username, password):
    res = requests.post(
        f"{BASE_URL}/login/",
        json={"username": username, "password": password},
    )
    if res.status_code != 200:
        raise Exception("Invalid credentials")
    save_token(res.json()["token"])


def get_history():
    res = requests.get(f"{BASE_URL}/history/", headers=headers())
    res.raise_for_status()
    return res.json()


def upload_csv(file_path):
    with open(file_path, "rb") as f:
        res = requests.post(
            f"{BASE_URL}/upload-csv/",
            files={"file": f},
            headers=headers(),
        )
    res.raise_for_status()
    return res.json()


def download_pdf(dataset_id, save_path):
    res = requests.get(
        f"{BASE_URL}/report/{dataset_id}/",
        headers=headers(),
        stream=True,
    )
    res.raise_for_status()
    with open(save_path, "wb") as f:
        for chunk in res.iter_content(1024):
            f.write(chunk)
def logout():
    clear_token()
