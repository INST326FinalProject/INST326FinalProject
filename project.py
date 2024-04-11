import datetime

class Expense:
    """Class to represent an expense."""

    def __init__(self, amount, category, description):
        """
        Initialize an expense object.

        Parameters:
        - amount (float): The amount of the expense.
        - category (str): The category of the expense.
        - description (str): Description of the expense.
        """
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.datetime.now()

class BudgetApp:
    """Class to represent a budgeting and expense tracking application."""

    def __init__(self):
        """Initialize a BudgetApp object."""
        self.expenses = []  # List to store expense objects
        self.monthly_budgets = {}  # Dictionary to store monthly budgets

    def add_expense(self, amount, category, description):
        """
        Add an expense to the list of expenses.

        Parameters:
        - amount (float): The amount of the expense.
        - category (str): The category of the expense.
        - description (str): Description of the expense.
        """
        expense = Expense(amount, category, description)
        self.expenses.append(expense)

    def add_expense_auto(self, amount, category, description):
        """
        Add an expense automatically with the current date.

        Parameters:
        - amount (float): The amount of the expense.
        - category (str): The category of the expense.
        - description (str): Description of the expense.
        """
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        print(f"Automatically added expense of ${amount} to {category} on {expense.date}")

    def display_spending_breakdown(self):
        """Display spending breakdown by category."""
        categories = {}
        for expense in self.expenses:
            categories[expense.category] = categories.get(expense.category, 0) + expense.amount
        for category, amount in categories.items():
            print(f"{category}: ${amount}")

    def notify_spending_limit(self, limit):
        """
        Notify the user if they have exceeded the spending limit.

        Parameters:
        - limit (float): The spending limit.
        """
        total_spent = sum(expense.amount for expense in self.expenses)
        if total_spent > limit:
            print("You have exceeded your spending limit!")

    def set_monthly_budget(self, category, amount):
        """
        Set the monthly budget for a specific category.

        Parameters:
        - category (str): The category for which the budget is being set.
        - amount (float): The budget amount.
        """
        self.monthly_budgets[category] = amount
        print(f"Monthly budget for {category}: ${amount}")

    def provide_financial_tips(self):
        """Provide some generic financial tips."""
        print("Here are some financial tips:")
        print("- Track your expenses regularly.")
        print("- Try to allocate your budget wisely.")
        print("- Look for discounts and deals when shopping.")
        print("- Consider saving a portion of your income for emergencies.")
        print("- Avoid unnecessary impulse purchases.")
        print("- Consider investing for long-term financial goals.")

def main():
    app = BudgetApp()
    print("Welcome to BudgetApp!")
    while True:
        print("\n1. Add Expense")
        print("2. Display Spending Breakdown")
        print("3. Set Monthly Budget")
        print("4. Get Financial Tips")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                try:
                    amount = float(input("Enter the amount of the expense: "))
                    break
                except ValueError:
                    print("Error: Invalid input. Please enter a valid amount.")
            category = input("Enter the category of the expense: ")
            description = input("Enter the description of the expense: ")
            app.add_expense(amount, category, description)
        elif choice == '2':
            print("\nSpending Breakdown:")
            app.display_spending_breakdown()
        elif choice == '3':
            while True:
                try:
                    category = input("Enter the category for the monthly budget: ")
                    amount = float(input("Enter the monthly budget amount: "))
                    break
                except ValueError:
                    print("Error: Invalid input. Please enter a valid amount.")
            app.set_monthly_budget(category, amount)
        elif choice == '4':
            app.provide_financial_tips()
        elif choice == '5':
            print("Thank you for using BudgetApp!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
