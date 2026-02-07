# ⚗️ Chemical Equipment Parameter Visualizer

A full-stack application that allows users to **upload CSV files containing chemical equipment data**, automatically **analyze parameters**, **visualize results**, and **download PDF reports**.  
The project includes both a **Web Application** and a **Desktop Application**, powered by a common backend.

---

## 📌 Project Overview

The Chemical Equipment Parameter Visualizer helps users to:
- Upload CSV datasets
- View computed summaries
- Visualize equipment distributions using charts
- Maintain upload history
- Download PDF reports
- Access the system via Web or Desktop

---

## 🧱 Tech Stack

### Backend
- Django
- Django REST Framework
- Token Authentication
- PDF generation

### Web Frontend
- React.js
- Axios
- Chart.js
- CSS (Dark / Light mode)

### Desktop Application
- Python
- PyQt5
- Matplotlib
- Requests

---

## ✨ Features

- 🔐 Secure login (token-based)
- 📂 CSV upload & validation
- 📊 Dataset summary:
  - Total Count
  - Average Flowrate
  - Average Pressure
  - Average Temperature
  - Equipment Type Distribution
- 📈 Interactive bar charts with hover tooltips
- 🕘 Dataset upload history
- 📄 PDF report download
- 🌙 Dark / Light mode (Web & Desktop)
- 🔄 Auto-refresh after upload
- 💻 Desktop app with modern UI

---

## 🔑 Demo Login Credentials 

To make testing easy, the following **demo account** is provided:

Username: user
Password: nagamani@9014


These credentials work for:
- Web Application
- Desktop Application

> ⚠️ Credentials are provided **only for evaluation purposes**.


## 🛠 Create Your Own User (Optional)

If you prefer to use your own account:


cd backend
source venv/bin/activate
python manage.py createsuperuser

🚀 How to Run the Project

1️⃣ Backend (Django)

cd backend
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Backend runs at:

http://127.0.0.1:8000/


2️⃣ Web Application (React)

cd frontend
npm install
npm start

Web app runs at:

http://localhost:3000/


3️⃣ Desktop Application (PyQt5)

cd desktop_app

source venv/bin/activate
pip install -r requirements.txt

python main.py

🧪 Sample CSV Format

Equipment Name,Type,Flowrate,Pressure,Temperature
Pump A,Pump,45.5,5.2,120
Valve B,Valve,30.0,4.1,110
Compressor A,Compressor,60.0,6.5,140
HeatExchanger A,HeatExchanger,55.0,5.8,130
Large CSV files are supported.

📄 API Endpoints

Method	Endpoint	Description
POST	/api/login/	Login
POST	/api/upload-csv/	Upload CSV
GET	/api/history/	Dataset history
GET	/api/report/{id}/	Download PDF

🗂 Project Structure

chemical-visualizer/
│
├── backend/          # Django backend
├── frontend/         # React web app
├── desktop_app/      # PyQt5 desktop app
├── README.md


📝 Notes for Reviewers

Backend must be running before using Web or Desktop applications

Summary and charts appear only after selecting a dataset

Desktop app supports auto-login using saved token

Web and Desktop share the same backend APIs

