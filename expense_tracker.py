import json
import os
from datetime import datetime

file_name = "expenses.json"

def load_expenses():
    #if file does not exist, then create file and return empty list
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            json.dump([],f)
        return []
    #if file exists, return the file contents
    with open(file_name, "r") as f:
        return json.load(f)

def save_expenses(expenses):
    #.dump() converts from python to json, .load() converts from json to python
    with open(file_name,"w") as f:
        json.dump(expenses,f,indent=4)

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category of expense: ")
    amount = float(input("Enter amount ($): "))
    description = input("Enter description: ")
    
    expenses = load_expenses()
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
        
    })
    save_expenses(expenses)
    print("Expense added")

def view_expense():
    expenses = load_expenses()
    if not expenses:
        print("No expenses")
    else:
        #enumerate is like range() but gives both the index and item in the list
        #(expenses,1) --> starts from 1 instead of 0, is more natural for user
        for i, expense in enumerate(expenses,1):
            print(f"{i}. {expense['date']} | {expense['category']} | ${expense['amount']} | {expense['description']}")

def delete_expenses():
    expenses = load_expenses()
    view_expense()
    try:
        idx = int(input("Enter which number expense to delete: "))
        #because in view_expense(), the list of expenses begins at 1
        idx = idx - 1
        #checks if idx is valid
        if  idx >= 0 and idx < len(expenses):
            #.pop() removes and returns the item in the list
            deleted = expenses.pop(idx)
            save_expenses(expenses)
            print(f"Deleted: {deleted}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

def monthly_total():
    expenses = load_expenses()
    user_input = input("Enter month to view (YYYY-MM), or press Enter for current month: ").strip()
    if not user_input:
        current_month = datetime.now().strftime("%Y-%m")
    else:
        try:
            # Validate input format
            datetime.strptime(user_input, "%Y-%m")
            current_month = user_input
        except ValueError:
            print("Invalid format. Please enter in YYYY-MM format.")
            return
    total = 0.0
    for exp in expenses:
        if exp["date"].startswith(current_month):
            total = total + exp["amount"]
    print(f"Total expenses for {current_month}: ${total:.2f}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. View Monthly Total")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            delete_expenses()
        elif choice == "4":
            monthly_total()
        elif choice == "5":
            print("You have exited. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()