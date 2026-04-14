from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# 🔗 Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@chaituz12345",  
    database="student_db"
)

cursor = db.cursor()

# 🎯 Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'F'

# 🏠 Home Page
@app.route('/')
def index():
    return render_template('index.html')

# ➕ Add Student
@app.route('/add', methods=['POST'])
def add():
    roll = request.form['roll']
    name = request.form['name']
    m1 = int(request.form['m1'])
    m2 = int(request.form['m2'])
    m3 = int(request.form['m3'])

    total = m1 + m2 + m3
    percentage = total / 3
    grade = calculate_grade(percentage)

    query = """INSERT INTO students 
    (roll_no, name, marks1, marks2, marks3, total, percentage, grade) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

    values = (roll, name, m1, m2, m3, total, percentage, grade)
    
    cursor.execute(query, values)
    db.commit()

    return "✅ Student Added Successfully!"

# 🔍 Search Student
@app.route('/search', methods=['POST'])
def search():
    roll = request.form['roll']

    query = "SELECT * FROM students WHERE roll_no=%s"
    cursor.execute(query, (roll,))
    data = cursor.fetchone()

    return render_template('result.html', student=data)

# ▶️ Run App
if __name__ == '__main__':
    app.run(debug=True)
