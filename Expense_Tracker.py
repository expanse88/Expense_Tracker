import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    amount = float(input("Add your amount:\n"))
    category = input("Enter Category (e.g., food, transport): ")
    date = input("Enter date (YYYY-MM-DD): ")

    expenses.append({"amount": amount, "category": category, "date": date})
    save_expenses(expenses)
    print("Expense Added!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("\n---- All Expenses ----")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ${expense['amount']} - {expense['category']} on {expense['date']}")

def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Spend Your Money Wisely. Goodbye!")
            break
        else:
            print("Invalid Choice! Try Again.")

if __name__ == "__main__":
    main()
