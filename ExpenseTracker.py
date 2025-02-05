#1 create dictionary of expenses
expenses = {}

#Function to Add a Task
def add_expense(name, amount):
    expenses[name] = amount
    print(f"Expense '{name}' added with amount {amount}.")
