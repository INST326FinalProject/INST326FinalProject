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
        
    def calculate_monthly_spending(self, month, year): 
        """ Calculate the total amount spent in a given month. 
        
        Parameters: 
        - month (int): The month for which spending is calculated (1-12). 
        - year (int): The year for which spending is calculated. """ 
        total_spent = sum(expense.amount for expense in self.expenses if expense.date.month == month and expense.date.year == year) 
        print(f"Total spent in {datetime.datetime(month=month, year=year, day=1).strftime('%B %Y')}: ${total_spent}")

def main():
    app = BudgetApp()
    print("Welcome to BudgetApp!")
    while True:
        print("\n1. Add Expense")
        print("2. Display Spending Breakdown")
        print("3. Set Monthly Budget")
        print("4. Get Financial Tips")
        print("5. Calculate Monthly Spending")
        print("6. Exit")
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
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year: "))
            app.calculate_monthly_spending(month, year)
        elif choice == '6':
            print("Thank you for using BudgetApp!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
def provide_financial_tips(self):
        """Provide financial tips based on spending patterns."""
        categories = {}
        for expense in self.expenses:
            categories[expense.category] = categories.get(expense.category, 0) + expense.amount

        print("Here are some financial tips based on your spending patterns:")
        if categories.get("Food", 0) > 0.3 * sum(categories.values()):
            print("- Consider reducing your spending on food. Try cooking at home more often.")
        if categories.get("Transportation", 0) > 0.2 * sum(categories.values()):
            print("- Look for cheaper transportation options or consider carpooling.")
        if categories.get("Entertainment", 0) > 0.1 * sum(categories.values()):
            print("- Be mindful of your entertainment expenses. Consider free or low-cost activities.")
        if categories.get("Shopping", 0) > 0.2 * sum(categories.values()):
            print("- Avoid impulse purchases and stick to your shopping list to save money.")
        if categories.get("Utilities", 0) > 0.1 * sum(categories.values()):
            print("- Try to reduce your utility bills by being more energy-efficient.")
        if categories.get("Healthcare", 0) > 0.1 * sum(categories.values()):
            print("- Review your healthcare expenses and see if there are ways to save on medical costs.")
        if categories.get("Other", 0) > 0.1 * sum(categories.values()):
            print("- Keep track of miscellaneous expenses to ensure they don't add up.")