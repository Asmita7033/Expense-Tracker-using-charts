#  Expense Tracker with Charts

A **full-stack Expense Tracker Web Application** that allows users to manage daily expenses, apply filters, and visualize spending using interactive charts.
Built using **Flask + SQLite** for backend and **HTML, CSS, JavaScript + Chart.js** for frontend.

This project demonstrates real-world concepts like REST APIs, CRUD operations, data aggregation, and frontend-backend integration — perfect for learning or portfolio showcase.

---

## ✨ Features

### ✅ Core Features (MVP)

* Add new expenses with description, amount, category & date
* View expenses in a dynamic table
* Delete expenses instantly
* Filter by category and date
* Automatic total calculation
* Pie chart visualization using Chart.js

### ⭐ Advanced Features (Optional Enhancements)

* Edit/update expenses
* Date range filtering
* Weekly or monthly analytics
* CSV export support
* Budget alerts
* Responsive UI improvements

---

## 🧰 Tech Stack

### 🔹 Backend

* Flask (Python Web Framework)
* SQLite Database
* Flask-CORS

### 🔹 Frontend

* HTML5
* CSS3
*  JavaScript
* Chart.js

---

## 📂 Project Structure

```
expense-tracker-with-charts/
│
├── backend/
│   ├── app.py
│   ├── database.db
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/expense-tracker-with-charts.git
cd expense-tracker-with-charts
```

---

### 2️⃣ Backend Setup

Create virtual environment:

```
python -m venv venv
```

Activate environment:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install flask flask-cors
```

Run Flask server:

```
python app.py
```

Backend will run on:

```
http://localhost:5000
```

---

### 3️⃣ Frontend Setup

Simply open:

```
frontend/index.html
```

OR use Live Server extension in VS Code.

---

## 🔌 API Endpoints

### Expense APIs

| Method | Endpoint       | Description        |
| ------ | -------------- | ------------------ |
| POST   | /api/expenses  | Add new expense    |
| GET    | /api/expenses  | Get all expenses   |
| GET    | /api/expenses/ | Get single expense |
| PUT    | /api/expenses/ | Update expense     |
| DELETE | /api/expenses/ | Delete expense     |

### Stats APIs

| Method | Endpoint               | Description     |
| ------ | ---------------------- | --------------- |
| GET    | /api/stats/by-category | Category totals |
| GET    | /api/stats/total       | Overall totals  |

---

## 🧠 Core Concepts Demonstrated

* REST API Design
* CRUD Operations
* SQL Aggregation Queries
* Input Validation & Error Handling
* Dynamic DOM Rendering
* Data Visualization with Chart.js

Example SQL Aggregation:

```
SELECT category, SUM(amount) FROM expenses GROUP BY category;
```

---

## 🗺️ Project Roadmap

* Expense CRUD APIs
* Expense Table UI
* Pie Chart Integration
* CSV Export Feature
* Authentication System
* Dark Mode UI

---

## 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.

---

## 👩‍💻 Author

**Asmita Pandey**
Project Manager & Developer Team

---

## 📄 License

This project is created for **educational and portfolio purposes**.
