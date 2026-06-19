import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="K@rthik123",
    database="expense_tracker"
)
cursor=conn.cursor()
cursor.execute("SELECT SUM(amount) FROM transaction where type='Income'")
income=cursor.fetchone()[0]
cursor.execute("SELECT SUM(amount) FROM transaction where type='Expense'")
expense=cursor.fetchone()[0]
income = income if income else 0
expense = expense if expense else 0
print("Total Income:", income)
print("Total Expense:", expense)
print("Balance:", income-expense)