import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="K@rthik123",
    database="expense_tracker"
)
cursor=conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS transaction(
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   type VARCHAR(20),
                   amount DECIMAL(10,2),
                   category VARCHAR(50),
                   transaction_date DATE
               )""")
print("Table Created Successfully")