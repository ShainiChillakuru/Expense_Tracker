import os
while True:
    print("\n==== EXPENSE TRACKER ====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Monthly Report")
    print("5. Exit")
    choice = int(input("Enter Choice:"))
    if choice==1:
        os.system("python add_income.py")
    elif choice==2:
        os.system("python add_expense.py")
    elif choice==3:
        os.system("python view_transactions.py")
    elif choice ==4:
        os.system("python monthly_report.py")
        break
    else:
        print("Invalid Choice")