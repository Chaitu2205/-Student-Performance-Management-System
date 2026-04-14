# -Student-Performance-Management-System
# 🎓 Student Result Management System

A full-stack web application to manage student academic records, calculate results, and visualize performance using charts.

---

## 📌 Features

* ➕ Add student details (Roll No, Name, Marks)
* 📊 Automatically calculate Total, Percentage, and Grade
* 🔍 Search student by Roll Number
* 📈 Visualize marks using interactive bar charts (Chart.js)
* 🎨 Modern UI with responsive design

---

## 🛠️ Technologies Used

* Frontend: HTML, CSS
* Backend: Python (Flask)
* Database: MySQL
* Visualization: Chart.js

---

## 🧠 How It Works

1. User enters student details through the form
2. Backend processes data using Flask
3. Marks are stored in MySQL database
4. System calculates total, percentage, and grade
5. Data is retrieved and displayed with a chart

---

## 📂 Project Structure

Student_folder/
│
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

1. Install dependencies:
   pip install flask mysql-connector-python

2. Setup MySQL database:
   CREATE DATABASE student_db;
   USE student_db;

CREATE TABLE students (
roll_no INT PRIMARY KEY,
name VARCHAR(50),
marks1 INT,
marks2 INT,
marks3 INT,
total INT,
percentage FLOAT,
grade VARCHAR(5)
);

3. Update MySQL credentials in app.py

4. Run the application:
   python app.py

5. Open in browser:
   http://127.0.0.1:5000

---

## 📊 Sample Output

* Add student data
* View results
* Analyze marks using charts

---

## 🚀 Future Enhancements

* 🔐 Login & Authentication system
* 📊 Dashboard for multiple students
* 📈 Advanced analytics
* 🌐 Deployment on cloud

---

## 👨‍💻 Author

S. Chaitanya
B.Tech CSE (Data Science)
Skills: Python, HTML, CSS, SQL

---

## 💬 Description

This project demonstrates full-stack development skills, database integration, and data visualization, making it suitable for beginner to intermediate level developers.

