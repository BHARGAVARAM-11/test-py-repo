##Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]

#app.py
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="student_mysql",
    user="root",
    password="rootpass",
    database="student_db"
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")

# Insert students
students = [
    (100, 'Bhargav', 22),
    (99, 'Phani', 24),
    (98, 'Tarun', 25)
]

cursor.executemany("INSERT INTO students (student_id, name, age) VALUES (%s, %s, %s)", students)
conn.commit()

# Fetch and print
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
