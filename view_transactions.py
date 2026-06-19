import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="K@rthik123",
    database="expense_tracker"
)
cursor=conn.cursor()
cursor.execute("SELECT * FROM transaction")
records=cursor.fetchall()
for row in records:
    print(row)