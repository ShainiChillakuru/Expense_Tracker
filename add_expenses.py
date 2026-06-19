import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="K@rthik123",
    database="expense_tracker"
)
cursor=conn.cursor()
amount=float(input("Enter Expense Amount:"))
category=input("Enter Category:")
date=input("Enter Date (YYYY-MM-DD):")
query="""
INSERT INTO transaction
(type,amount,category,transaction_date)
VALUES(%s,%s,%s,%s)"""
values=("Expense",amount,category,date)
cursor.execute(query,values)
conn.commit()
print("Expense Added Successfully")