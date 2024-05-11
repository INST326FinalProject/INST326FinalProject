import datetime
import json

class Expense:
    """Class to represent an expense."""

    def __init__(self, amount, category, description, date=None):
        """
        Initialize an expense object.

        Parameters:
        - amount (float): The amount of the expense.
        - category (str): The category of the expense.
        - description (str): Description of the expense.
        - date (datetime.datetime, optional): The date of the expense. Defaults to now.
        """
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date if date is not None else datetime.datetime.now()

class BudgetApp:
    """Class to represent a budgeting and expense tracking application."""

    def __init__(self):
        """Initialize a BudgetApp object."""
        self.expenses = []  # List to store expense objects
        self.monthly_budgets = {}  # Dictionary to store monthly budgets
        self.goals = []

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
    
    def check_budget_limits(self):
        """Check if spending is nearing the set limit for any category."""
        for category, budget in self.monthly_budgets.items():
            spent = sum(expense.amount for expense in self.expenses if expense.category == category)
            if spent / budget >= 0.9:  # 90% of budget spent
                print(f"Alert: You've spent 90% of your budget for {category}!")
        
    def calculate_monthly_spending(self, month, year): 
        """ Calculate the total amount spent in a given month. 
        
        Parameters: 
        - month (int): The month for which spending is calculated (1-12). 
        - year (int): The year for which spending is calculated. """ 
        total_spent = sum(expense.amount for expense in self.expenses if expense.date.month == month and expense.date.year == year)
        return total_spent
        
    def save_data(self, filepath='expenses_data.json'):
        """Save expenses and monthly budgets to a file."""
        data = {
            'expenses': [{'amount': e.amount, 'category': e.category, 'description': e.description, 'date': e.date.strftime('%Y-%m-%d %H:%M:%S')} for e in self.expenses],
            'monthly_budgets': self.monthly_budgets
        }
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self, filepath='expenses_data.json'):
        """Load expenses and monthly budgets from a file."""
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                self.expenses = [
                    Expense(
                        expense['amount'], 
                        expense['category'], 
                        expense['description'], 
                        datetime.datetime.strptime(expense['date'], '%Y-%m-%d %H:%M:%S')
                    ) for expense in data['expenses']
                ]
                self.monthly_budgets = data['monthly_budgets']
        except FileNotFoundError:
            print("No previous data found. Starting fresh.")
    
    def provide_financial_tips(self):
        """Provide financial tips based on spending patterns and return them as a string."""
        categories = {}
        tips = []
        for expense in self.expenses:
            categories[expense.category] = categories.get(expense.category, 0) + expense.amount
        if categories.get("Food", 0) > 0.3 * sum(categories.values()):
            tips.append("- Consider reducing your spending on food. Try cooking at home more often.")
        if categories.get("Transportation", 0) > 0.2 * sum(categories.values()):
            tips.append("- Look for cheaper transportation options or consider carpooling.")
        if categories.get("Entertainment", 0) > 0.1 * sum(categories.values()):
            tips.append("- Be mindful of your entertainment expenses. Consider free or low-cost activities.")
        if categories.get("Shopping", 0) > 0.2 * sum(categories.values()):
            tips.append("- Avoid impulse purchases and stick to your shopping list to save money.")
        if categories.get("Utilities", 0) > 0.1 * sum(categories.values()):
            tips.append("- Try to reduce your utility bills by being more energy-efficient.")
        if categories.get("Healthcare", 0) > 0.1 * sum(categories.values()):
            tips.append("- Review your healthcare expenses and see if there are ways to save on medical costs.")
        if categories.get("Other", 0) > 0.1 * sum(categories.values()):
            tips.append("- Keep track of miscellaneous expenses to ensure they don't add up.")
        return "\n".join(tips)






