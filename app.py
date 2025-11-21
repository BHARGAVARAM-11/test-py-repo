import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="YOUR_RENDER_MYSQL_HOST",
    user="YOUR_RENDER_DB_USER",
    password="YOUR_RENDER_DB_PASSWORD",
    database="YOUR_RENDER_DB_NAME"

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
