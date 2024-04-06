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
