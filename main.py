from budget_app import BudgetApp
import data_manager

def main():
    # Load existing data
    expenses, monthly_budgets = data_manager.load_data()
    app = BudgetApp(expenses, monthly_budgets)

    # Your application logic here, e.g., CLI or GUI loop

    # Example: After adding an expense
    app.add_expense(100, 'Groceries', 'Weekly food')
    data_manager.save_data(app.expenses, app.monthly_budgets)

if __name__ == "__main__":
    main()
