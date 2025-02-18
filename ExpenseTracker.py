from datetime import datetime

#1 create dictionary of expenses
expenses = {}

#Function to Add a Task
def add_expense(name, category, amount, date):
    expenses[name] = {
        "category": category,
        "amount": amount,
        "date": date
    }
    print(f"Expense '{name}' added under '{category}' category with amount ${amount:.2f} on {date}.")

# Function to view expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nYour Expenses:")
    for name, details in expenses.items():
        print(f"🏷 {name} | Category: {details['category']} | Amount: ${details['amount']:.2f} | Date: {details['date']}")

# Function to calculate expenses
def total_expenses():
    total = sum(details["amount"] for details in expenses.values())
    print(f"\nTotal Expenses: ${total:.2f}")

# Main function to view menu
def main():
    while True:
        print("EXPENSE TRACKER MENU")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. View total expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter expense name (e.g., Rent, Groceries, etc.): ")
            category = input("Enter expense category (e.g., Food, Rent, Travel): ")
            
            while True:
                try:
                    amount = float(input("Enter amount: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
            
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            if not date:
                date = datetime.today().strftime('%Y-%m-%d')

            add_expense(name, category, amount, date)

        elif choice == "2":
            view_expenses()
        
        elif choice == "3":
            total_expenses()
        
        elif choice == "4":
            print("Exiting. Thank you for using the Expense Tracker!")
            break
        
        else:
            print("Invalid option! Please choose a valid number (1-4).")

main()

