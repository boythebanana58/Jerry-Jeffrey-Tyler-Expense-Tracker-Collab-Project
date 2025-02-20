# Jerry-Jeffrey-Tyler-Expense-Tracker-Collab-Project

## Instructions:
 - **Add Expense**: Enter a category, amount, and date in YYYY-MM-DD format.
 - **View All Expenses**: Displays all recorded expenses.
 - **Filter Expenses**: Shows expenses for a selected category.
 - **Calculate Total**: Displays the total amount spent.
 - **Delete Expense**: 
    - Enter a date (YYYY-MM-DD).
    - If expenses exist for that date, they will be removed.
    - If no matching expenses are found, you will be prompted to try again.
- **Exit**: Closes the program.

## Responsibilities/Credits

 - Jeffrey - handles adding expenses.
 - Jerry - implements the calculation of total expenses.
 - Tyler - works on filtering or deleting expenses.


## Reflection

Roles & Tasks
- Jeffrey - handles adding expenses.
- Jerry - implements the calculation of total expenses.
- Tyler - works on filtering or deleting expenses.

Challenges & Solutions
Handling incorrect inputs in adding expenses - Implemented validation checks for amount and date formats.
Not remembering the categories and dates of expenses to categorize or delete them: Improved the categorize and delete by making them print all expenses first.
How to make the user experience better so we don't need to press enter after doing everything: Used `time.sleep(1)` to automatically send the user back to the menu.

Collaboration Experience
We enjoyed collaborative coding because it allowed us to learn from each other and allowed us to complete this project faster. However, merging different styles of coding was sometimes a challenge when combining them all. Overall, working together helped us develop a more robust and user-friendly program.