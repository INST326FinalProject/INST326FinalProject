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

# Example usage
if __name__ == "__main__":
    app = BudgetApp()

    # Adding expenses
    app.add_expense(50, "Food", "Lunch")
    app.add_expense(30, "Transportation", "Uber")
    app.add_expense(100, "Entertainment", "Movie tickets")

    # Displaying spending breakdown
    print("Spending Breakdown:")
    app.display_spending_breakdown()

    # Setting spending limit and notifying
    app.notify_spending_limit(150)

    # Setting monthly budget
    app.set_monthly_budget("Food", 200)

    # Providing financial tips
    app.provide_financial_tips()
