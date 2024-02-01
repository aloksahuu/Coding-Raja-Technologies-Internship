import os
import json
from tabulate import tabulate

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return {'income': 0, 'expenses': []}

def save_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

def add_income(data):
    income_amount = float(input("Enter income amount: "))
    data['income'] += income_amount
    print(f"Income of ${income_amount} added successfully.")

def add_expense(data):
    category = input("Enter expense category: ")
    expense_amount = float(input("Enter expense amount: "))
    data['expenses'].append({'category': category, 'amount': expense_amount})
    print(f"Expense of ${expense_amount} under category '{category}' added successfully.")

def calculate_budget(data):
    total_expenses = sum(expense['amount'] for expense in data['expenses'])
    remaining_budget = data['income'] - total_expenses
    return remaining_budget

def analyze_expenses(data):
    expenses_by_category = {}
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category not in expenses_by_category:
            expenses_by_category[category] = 0
        expenses_by_category[category] += amount

    print("\nExpense Analysis:")
    headers = ["Category", "Total Amount"]
    rows = [[category, amount] for category, amount in expenses_by_category.items()]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

def main():
    file_path = 'budget_data.json'
    data = load_data(file_path)

    while True:
        print("\n===== Budget Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Remaining Budget")
        print("4. Expense Analysis")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))


        if choice == 1:
            add_income(data)
        elif choice == 2:
            add_expense(data)
        elif choice == 3:
            remaining_budget = calculate_budget(data)
            print(f"\nRemaining Budget: ${remaining_budget}")
        elif choice == 4:
            analyze_expenses(data)
        elif choice == 5:
            save_data(data, file_path)
            print("Budget data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
