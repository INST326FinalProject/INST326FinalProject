import datetime

class Expense:
    """Class to represent an expense
    """
    def __init__(self, amount, category, description):
        """Initialize an expense object
        
        Args:
            amount (float): the amount of the expense
            category (str): the category of the expense
            description (str): description of the expense
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

