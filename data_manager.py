import json
import datetime
from budget_app import Expense  # Ensure this import statement is correct based on your project structure

def save_data(expenses, monthly_budgets, filepath='expenses_data.json'):
    """Save expenses and monthly budgets to a file."""
    data = {
        'expenses': [{'amount': e.amount, 'category': e.category, 'description': e.description, 'date': e.date.strftime('%Y-%m-%d %H:%M:%S')} for e in expenses],
        'monthly_budgets': monthly_budgets
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def load_data(filepath='expenses_data.json'):
    """Load expenses and monthly budgets from a file."""
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            expenses = [Expense(expense['amount'], expense['category'], expense['description'], datetime.datetime.strptime(expense['date'], '%Y-%m-%d %H:%M:%S')) for expense in data['expenses']]
            monthly_budgets = data['monthly_budgets']
            return expenses, monthly_budgets
    except FileNotFoundError:
        print("No previous data found. Starting fresh.")
        return [], {}
