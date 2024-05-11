import tkinter as tk
from tkinter import messagebox, simpledialog, Scrollbar, Canvas, Frame
from budget_app import BudgetApp
import datetime

class BudgetAppGUI:
    def __init__(self, master):
        self.master = master
        self.app = BudgetApp()
        self.app.load_data()

        master.title("EduWallet")
        
        # Create a canvas and a vertical scrollbar
        canvas = Canvas(master)
        scrollbar = Scrollbar(master, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)
        
        # Configure the canvas to use the scrollbar
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Grid the canvas and scrollbar
        canvas.grid(row=0, column=0, sticky="news")
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        # Making the grid expandable
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # Setup for expense entry
        tk.Label(scrollable_frame, text="Amount:").grid(row=0)
        tk.Label(scrollable_frame, text="Category:").grid(row=1)
        tk.Label(scrollable_frame, text="Description:").grid(row=2)

        self.amount_entry = tk.Entry(scrollable_frame)
        self.category_entry = tk.Entry(scrollable_frame)
        self.description_entry = tk.Entry(scrollable_frame)

        self.amount_entry.grid(row=0, column=1)
        self.category_entry.grid(row=1, column=1)
        self.description_entry.grid(row=2, column=1)

        # Buttons to interact with the app
        tk.Button(scrollable_frame, text="Add Expense", command=self.add_expense).grid(row=3, columnspan=2)
        tk.Button(scrollable_frame, text="Show Spending Breakdown", command=self.show_spending_breakdown).grid(row=4, columnspan=2)
        tk.Button(scrollable_frame, text="Set Monthly Budget", command=self.set_monthly_budget).grid(row=5, columnspan=2)
        tk.Button(scrollable_frame, text="Show Financial Tips", command=self.show_financial_tips).grid(row=7, columnspan=2)
        tk.Button(scrollable_frame, text="Calculate Monthly Spending", command=self.calculate_monthly_spending).grid(row=6, columnspan=2)
        tk.Button(scrollable_frame, text="Save Data", command=self.save_data).grid(row=8, columnspan=2)

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            description = self.description_entry.get()
            self.app.add_expense(amount, category, description)
            self.app.save_data()
            messagebox.showinfo("Success", "Expense added successfully.")
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.check_budget_limits()  # Check budget limits after adding an expense
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")

    def show_spending_breakdown(self):
        categories = {}
        for expense in self.app.expenses:
            categories[expense.category] = categories.get(expense.category, 0) + expense.amount
        breakdown = '\n'.join([f"{cat}: ${amt:.2f}" for cat, amt in categories.items()])
        messagebox.showinfo("Spending Breakdown", breakdown)

    def set_monthly_budget(self):
        category = simpledialog.askstring("Input", "Enter category:", parent=self.master)
        if category:
            amount = simpledialog.askfloat("Input", f"Enter budget amount for {category}:", parent=self.master)
            if amount is not None:
                self.app.set_monthly_budget(category, amount)
                self.app.save_data()
                messagebox.showinfo("Success", f"Budget set for {category}: ${amount:.2f}")

    def show_financial_tips(self):
        tips = self.app.provide_financial_tips()
        if tips:
            messagebox.showinfo("Financial Tips", tips)
        else:
            messagebox.showinfo("Financial Tips", "No specific tips available based on your current spending.")

    def calculate_monthly_spending(self):
        month = simpledialog.askinteger("Input", "Enter month (1-12):", parent=self.master, minvalue=1, maxvalue=12)
        year = simpledialog.askinteger("Input", "Enter year:", parent=self.master, minvalue=2000, maxvalue=datetime.datetime.now().year)
        if month and year:
            self.app.calculate_monthly_spending(month, year)
    
    def check_budget_limits(self):
        for category, budget in self.app.monthly_budgets.items():
            spent = sum(expense.amount for expense in self.app.expenses if expense.category == category)
            if spent > budget:
                messagebox.showwarning("Budget Limit Exceeded", f"You have exceeded your budget for {category}!\nBudget: ${budget:.2f}\nSpent: ${spent:.2f}")

    def save_data(self):
        self.app.save_data()
        messagebox.showinfo("Data Saved", "All data has been saved to file.")

def main():
    root = tk.Tk()
    gui = BudgetAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
