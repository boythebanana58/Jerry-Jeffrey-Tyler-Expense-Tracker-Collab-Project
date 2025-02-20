import os  #importing os to interact with the operating system for clearing the screen
import time  #importing time to add delays
import datetime  #importing datetime to validate date inputs

#clears the terminal screen
def clear_screen():  #https://docs.python.org/3/library/os.html#os.system
    #checks operating system and uses the correct command
    if os.name == 'nt':  #Windows
        os.system('cls')
    else:  #Unix/Linux/Mac
        os.system('clear')

#list to store expenses
#https://docs.python.org/3/tutorial/datastructures.html
expenses = []

#adds a new expense with retry on invalid input
def add_expense():
    while True:
        category = input("Enter expense category (e.g., Food, Transport): ")
        #validate that the amount is a valid number
        try:
            amount = float(input("Enter expense amount: "))  #https://docs.python.org/3/library/functions.html#float
        except ValueError:
            print("Invalid input. Amount must be a valid number.\n")
            continue  #retry from the beginning of the loop

        #validate that the date is a real date in the correct format
        date_str = input("Enter expense date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid input. Date must be a real date in the format YYYY-MM-DD.\n")
            continue  # Retry from the beginning of the loop

        #if both validations pass, add the expense
        expense = {"category": category, "amount": amount, "date": date_str}
        expenses.append(expense)
        print("Expense added successfully!\n")
        time.sleep(1)
        break

#function to view all expenses (waits for user input before returning to menu)
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
    else:
        print("All Expenses:")
        #enumerate lists all expenses with an index
        #https://www.geeksforgeeks.org/enumerate-in-python/
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. Category: {expense['category']}, Amount: ${expense['amount']}, Date: {expense['date']}")
        print()
    input("Press Enter to return to the menu...")

#filter expenses by category with retry if no expenses match
def filter_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        time.sleep(1)
        return

    while True:
        #display all available categories in sorted order
        unique_categories = sorted(set(expense['category'] for expense in expenses))
        print("Available Categories:")
        for category in unique_categories:
            print(category)
        print()

        category = input("Enter category to filter by: ")
        filtered = [expense for expense in expenses if expense['category'].lower() == category.lower()]

        if not filtered:
            print("No expenses found for this category. Please try again.\n")
            time.sleep(1)
        else:
            print(f"Expenses in category '{category}':")
            for expense in filtered:
                print(f"Amount: ${expense['amount']}, Date: {expense['date']}")
            print()
            break
    input("Press Enter to return to the menu...")

#calculates total expenses
def calculate_total():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: ${total}\n")
    input("Press Enter to return to the menu...")

#delete an expense with retry if not found
def delete_expense():
    if not expenses:
        print("No expenses recorded.\n")
        time.sleep(1)
        return

    while True:
        #display all current expenses
        print("Current Expenses:")
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. Category: {expense['category']}, Amount: ${expense['amount']}, Date: {expense['date']}")
        print()

        #display available categories (sorted)
        unique_categories = sorted(set(expense['category'] for expense in expenses))
        print("Available Categories (sorted):")
        for category in unique_categories:
            print(category)
        print()

        category = input("Enter category of expense to delete: ")
        date = input("Enter date of expense to delete (YYYY-MM-DD): ")

        found = False
        for expense in expenses:
            if expense['category'].lower() == category.lower() and expense['date'] == date:
                expenses.remove(expense)
                print("Expense deleted successfully!\n")
                found = True
                break
        if found:
            break
        else:
            print("No matching expense found. Please try again.\n")
            time.sleep(1)
    input("Press Enter to return to the menu...")

#main program loop
def main():
    while True:
        clear_screen()  #clear the screen before showing the menu
        print("Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses by Category")
        print("4. Calculate Total Expenses")
        print("5. Delete an Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            clear_screen()
            add_expense()
        elif choice == "2":
            clear_screen()
            view_expenses()
        elif choice == "3":
            clear_screen()
            filter_expenses()
        elif choice == "4":
            clear_screen()
            calculate_total()
        elif choice == "5":
            clear_screen()
            delete_expense()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")
            time.sleep(1)

        #Brief delay for options other than viewing expenses
        if choice != "2":
            time.sleep(1)

main()