import tkinter as tk
from tkinter import simpledialog, messagebox
from budget_app import BudgetApp

class BudgetAppGUI:
    def __init__(self, master):
        self.master = master
        self.app = BudgetApp()
        self.app.load_data()

        master.title("BudgetApp")

        # Setup for expense entry
        tk.Label(master, text="Amount:").grid(row=0)
        tk.Label(master, text="Category:").grid(row=1)
        tk.Label(master, text="Description:").grid(row=2)

        self.amount_entry = tk.Entry(master)
        self.category_entry = tk.Entry(master)
        self.description_entry = tk.Entry(master)

        self.amount_entry.grid(row=0, column=1)
        self.category_entry.grid(row=1, column=1)
        self.description_entry.grid(row=2, column=1)

        # Button to add an expense
        tk.Button(master, text="Add Expense", command=self.add_expense).grid(row=3, columnspan=2)

        # Button to add a goal
        tk.Button(master, text="Add Goal", command=self.add_goal).grid(row=4, columnspan=2)

        # Button for contributing to a goal
        tk.Button(master, text="Contribute to Goal", command=self.contribute_to_goal).grid(row=5, columnspan=2)

        # Listbox to display goals
        self.goals_listbox = tk.Listbox(master)
        self.goals_listbox.grid(row=6, columnspan=2, sticky="ew")
        self.update_goals_listbox()

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            description = self.description_entry.get()
            self.app.add_expense(amount, category, description)
            self.check_budget_limits()
            self.app.save_data()
            messagebox.showinfo("Success", "Expense added successfully.")
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.update_goals_listbox()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")

    def add_goal(self):
        name = simpledialog.askstring("Input", "Goal name:", parent=self.master)
        target_amount = simpledialog.askfloat("Input", "Target amount:", parent=self.master)
        if name and target_amount:
            self.app.add_goal(name, target_amount, "2023-12-31")  # Simplified: Consider adding date picker for deadline
            self.update_goals_listbox()
            messagebox.showinfo("Success", "Goal added successfully.")
        else:
            messagebox.showerror("Error", "Invalid input for goal.")

    def contribute_to_goal(self):
        goal_names = [goal.name for goal in self.app.goals]
        goal_name = simpledialog.askstring("Contribute to Goal", "Enter goal name:", parent=self.master)
        if goal_name in goal_names:
            amount = simpledialog.askfloat("Contribute to Goal", "Enter amount:", parent=self.master)
            if amount:
                for goal in self.app.goals:
                    if goal.name == goal_name:
                        goal.add_contribution(amount)
                        self.update_goals_listbox()
                        self.app.save_data()
                        messagebox.showinfo("Success", f"Contributed ${amount} to {goal_name}.")
                        break
        else:
            messagebox.showerror("Error", "Goal not found.")

    def update_goals_listbox(self):
        self.goals_listbox.delete(0, tk.END)  # Clear current items
        for goal in self.app.goals:
            progress = (goal.current_amount / goal.target_amount) * 100 if goal.target_amount > 0 else 0
            self.goals_listbox.insert(tk.END, f"{goal.name}: {progress:.2f}% towards ${goal.target_amount}")

    def check_budget_limits(self):
        for category, budget in self.app.monthly_budgets.items():
            spent = sum(expense.amount for expense in self.app.expenses if expense.category == category)
            if spent >= budget * 0.9:  # Trigger alert at 90% of budget
                messagebox.showwarning("Budget Limit Alert", f"You have reached 90% of your {category} budget.")

def main():
    root = tk.Tk()
    gui = BudgetAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
