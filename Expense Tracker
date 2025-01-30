import csv
import os

FILE = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])  # Header row

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    description = input("Enter a short description: ")
    
    while True:
        try:
            amount = float(input("Enter amount: "))
            break 
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    
    print("Expense added!")
