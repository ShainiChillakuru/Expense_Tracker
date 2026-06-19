import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="K@rthik123"
)
cursor=conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS expense_tracker")
print("Database Created Successfully")