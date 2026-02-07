⚗️ Chemical Equipment Parameter Visualizer

A full-stack application to upload, analyze, visualize, and export chemical equipment datasets.
The project includes both a Web Application and a Desktop Application, backed by a Django REST API.

🚀 Features
✅ Common Features (Web & Desktop)

Secure login using Token Authentication

Upload large CSV datasets

Automatic dataset analysis:

Total equipment count

Average flowrate

Average pressure

Average temperature

Equipment type distribution

View upload history (latest datasets first)

Download PDF reports

Dark / Light theme support

Search datasets by name

🌐 Web Application (React)
Tech Stack

Frontend: React, Axios, Chart.js

Backend: Django, Django REST Framework

Auth: Token Authentication

Web Features

Interactive dashboard

Animated summary cards

Colorful bar charts with hover tooltips

Toast notifications

Responsive UI

Run Web App
# Backend
cd backend
python manage.py runserver

# Frontend
cd web-frontend
npm install
npm start

🖥️ Desktop Application (PyQt5)
Tech Stack

UI: PyQt5

Charts: Matplotlib

API: Django REST backend

Storage: Local token & theme persistence

Desktop Features

Native desktop UI

Auto-login using stored token

Upload CSV directly from file system

Dataset summary panel

Interactive bar chart with hover tooltips

PDF download

Dark / Light theme toggle

Toast notifications

Auto refresh after upload

Run Desktop App
cd desktop_app
python main.py

📊 Dataset Summary Metrics

For every uploaded CSV, the system computes:

Total Count

Average Flowrate

Average Pressure

Average Temperature

Equipment Type Distribution

These results are:

Shown visually (charts)

Displayed numerically

Included in downloadable PDF reports

📄 CSV Format

Example CSV structure:

Equipment Name,Type,Flowrate,Pressure,Temperature
Pump A,Pump,45.5,5.2,120
Valve B,Valve,32.5,4.3,112
Compressor A,Compressor,60.0,6.5,140
HeatExchanger A,HeatExchanger,55.0,5.8,135
Reactor A,Reactor,70.0,7.2,150

🔐 Authentication Flow

User logs in

Backend returns a token

Token is stored:

Web → localStorage

Desktop → local file

Token is sent with every API request

📦 API Endpoints
Method	Endpoint	Description
POST	/api/login/	User login
POST	/api/upload-csv/	Upload CSV
GET	/api/history/	Dataset history
GET	/api/report/<id>/	Download PDF
🧠 Architecture Overview
chemical-visualizer/
│
├── backend/          # Django REST API
│
├── web-frontend/     # React Web App
│
├── desktop_app/      # PyQt5 Desktop App
│
└── README.md

✅ Requirements Coverage

✔ CSV upload & validation
✔ Data analysis
✔ Charts & visualization
✔ PDF export
✔ Authentication
✔ Web UI
✔ Desktop UI
✔ Clean UI / UX
✔ Dark & Light themes

📌 Notes

Only the latest 5 datasets are retained (older ones are auto-deleted)

Large CSV files are supported

Backend is reusable for both clients

🏁 Conclusion

This project demonstrates:

Full-stack development

REST API design

Frontend visualization

Desktop application development

Clean UI/UX practices
