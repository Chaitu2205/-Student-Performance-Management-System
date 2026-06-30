# 🎓 Student Performance Management System
## 🚀 Live Demo

https://student-performance-management-system-bf9v.onrender.com/

# 📖 Overview

The **Student Performance Management System** is a full-stack web application developed to simplify student academic record management. The application enables users to add student information, calculate academic performance automatically, search student records instantly, and visualize subject-wise marks using interactive charts.

This project demonstrates practical implementation of **CRUD Operations**, **Database Integration**, **Backend Development**, and **Data Visualization**.

---

# ✨ Key Features

### 📌 Student Management
- Add new student records
- Store academic information securely
- Search students using Roll Number

### 📊 Automatic Result Generation
- Calculates Total Marks
- Calculates Percentage
- Assigns Grade Automatically

### 📈 Interactive Analytics
- Subject-wise Bar Chart
- Dynamic Visualization using Chart.js

### 💻 User Experience
- Responsive Modern UI
- Glassmorphism Design
- Clean User Interface

---

# 🖥️ Tech Stack

| Category | Technology |
|----------|------------|
| Frontend | HTML5, CSS3 |
| Backend | Python, Flask |
| Database | MySQL / TiDB Cloud |
| Charts | Chart.js |
| Deployment | Render |

---

# 🏗️ System Architecture

```
User
   │
   ▼
HTML/CSS Interface
   │
   ▼
Flask Application
   │
   ▼
Business Logic
   │
   ▼
MySQL / TiDB Cloud Database
   │
   ▼
Student Records
```

---

# 📂 Project Structure

```
Student-Performance-Management-System
│
├── app.py
├── requirements.txt
├── Procfile
├── isrgrootx1.pem
│
├── templates
│   ├── index.html
│   └── result.html
│
├── README.md
│
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YourUsername/Student-Performance-Management-System.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Database

Create Database

```sql
CREATE DATABASE student_db;
```

Create Table

```sql
CREATE TABLE students(
roll_no INT PRIMARY KEY,
name VARCHAR(50),
marks1 INT,
marks2 INT,
marks3 INT,
total INT,
percentage FLOAT,
grade VARCHAR(5)
);
```

---

## Run Project

```bash
python app.py
```

Open Browser

```
http://127.0.0.1:5000
```

---

# 📸 Application Workflow

```
Enter Student Details
        │
        ▼
Flask Processes Request
        │
        ▼
Calculate Result
        │
        ▼
Store in Database
        │
        ▼
Retrieve Student Record
        │
        ▼
Display Result + Graph
```

---

# 📊 Functional Modules

✔ Student Registration

✔ Student Search

✔ Automatic Grade Calculation

✔ Marks Visualization

✔ Database Management

---

# 📈 Sample Calculations

```
Total = Maths + Physics + Chemistry

Percentage = Total / 3

Grade

90+      → A

75-89    → B

50-74    → C

Below 50 → F
```

---

# 🚀 Future Enhancements

- Login Authentication
- Admin Dashboard
- Student Dashboard
- Edit/Delete Student Records
- Export PDF Result
- Email Notifications
- Attendance Module
- Semester-wise Analytics
- Responsive Dashboard
- Cloud Deployment

---

# 💡 Learning Outcomes

This project demonstrates knowledge of:

- Python Programming
- Flask Framework
- CRUD Operations
- SQL Queries
- MySQL Database
- TiDB Cloud
- Backend Development
- Web Application Development
- Data Visualization
- REST Concepts
- GitHub Project Management

---

# 👨‍💻 Developed By

## S. Chaitanya

B.Tech – Computer Science & Engineering (Data Science)

Python Developer | Data Science Enthusiast | Full Stack Learner

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository.

Fork it, contribute, and improve it.

---

# 📜 License

This project is developed for educational and portfolio purposes.
