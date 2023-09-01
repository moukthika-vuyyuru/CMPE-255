import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from expense_manager import ExpenseManager
from expense_tracker import ExpenseTracker
from expense_chart import ExpenseChart
from expense_io import ExpenseIO
from datetime import datetime
from ttkthemes import ThemedStyle

# The GUI class for Expense Tracker application using Tkinter
# This class is responsible for creating and managing the GUI elements and calling the appropriate methods in ExpenseManager
class ExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Apply themed style
        self.style = ThemedStyle(self.root)
        self.style.set_theme("arc")  # Choose the theme you like

        # Initialize ExpenseManager
        expense_tracker = ExpenseTracker()
        expense_chart = ExpenseChart(expense_tracker)
        expense_manager = ExpenseManager(expense_tracker, expense_chart)
        self.expense_io = ExpenseIO()
        self.expense_tracker = ExpenseManager(expense_tracker, expense_chart)
        
        # Create and place widgets
        self.create_widgets()
        self.pack_widgets()

        # Apply styling
        self.apply_styling()
    

    def apply_styling(self):
        # Apply styling to buttons
        buttons = [
            self.button_record, self.button_edit, self.button_delete,
            self.button_view_expenses, self.button_view_total_spending,
            self.button_view_spending_by_category, self.button_generate_chart,
            self.button_get_expenses_by_category,
            self.button_calculate_average_spending_by_category,
            self.button_get_top_spending_category,
            self.button_calculate_spending_trend,
            self.button_export_expenses_to_csv,
            self.button_import_expenses_from_csv
        ]
        for button in buttons:
            button.configure(
                bg="#4CAF50", fg="black", activebackground="#45a049",
                activeforeground="black", font=("Helvetica", 12), padx=10, pady=5
            )

        # Apply styling to labels
        labels = [self.label_amount, self.label_date, self.label_description, self.label_categories]
        for label in labels:
            label.configure(font=("Helvetica", 12))

        # Apply styling to entry fields
        entry_fields = [self.entry_amount, self.entry_date, self.entry_description, self.entry_categories]
        for entry in entry_fields:
            entry.configure(font=("Helvetica", 12))

        # Apply styling to result_text
        self.result_text.configure(font=("Helvetica", 12))

    # Create widgets
    def create_widgets(self):
        # Labels
        self.label_amount = tk.Label(self.root, text="Amount:")
        self.label_date = tk.Label(self.root, text="Date (YYYY-MM-DD):")
        self.label_description = tk.Label(self.root, text="Description:")
        self.label_categories = tk.Label(self.root, text="Categories (comma-separated):")

        # Entry fields
        self.entry_amount = tk.Entry(self.root)
        self.entry_date = tk.Entry(self.root)
        self.entry_description = tk.Entry(self.root)
        self.entry_categories = tk.Entry(self.root)

        # Buttons
        self.button_record = tk.Button(self
                                       .root, text="Record Expense", command=self.record_expense)
        self.button_edit = tk.Button(self.root, text="Edit Expense", command=self.edit_expense)
        self.button_delete = tk.Button(self.root, text="Delete Expense", command=self.delete_expense)
        self.button_view_expenses = tk.Button(self.root, text="View Expenses", command=self.view_expenses)
        self.button_view_total_spending = tk.Button(self.root, text="View Total Spending", command=self.view_total_spending)
        self.button_view_spending_by_category = tk.Button(self.root, text="View Spending by Category", command=self.view_spending_by_category)
        self.button_generate_chart = tk.Button(self.root, text="Generate Chart", command=self.generate_chart)
        self.button_get_expenses_by_category = tk.Button(self.root, text="Get Expenses by Category", command=self.get_expenses_by_category)
        self.button_calculate_average_spending_by_category = tk.Button(self.root, text="Calculate Average Spending by Category", command=self.calculate_average_spending_by_category)
        self.button_get_top_spending_category = tk.Button(self.root, text="Get Top Spending Category", command=self.get_top_spending_category)
        self.button_calculate_spending_trend = tk.Button(self.root, text="Calculate Spending Trend", command=self.calculate_spending_trend)
        self.button_export_expenses_to_csv = tk.Button(self.root, text="Export Expenses to CSV", command=self.export_expenses_to_csv)
        self.button_import_expenses_from_csv = tk.Button(self.root, text="Import Expenses from CSV", command=self.import_expenses_from_csv)

        # Result area
        self.result_text = tk.Text(self.root, height=10, width=50)

    # Pack widgets
    def pack_widgets(self):
        # Arrange widgets using grid layout

        self.label_amount.grid(row=1, column=0, sticky=tk.W)
        self.entry_amount.grid(row=1, column=1, padx=10)

        self.label_date.grid(row=2, column=0, sticky=tk.W)
        self.entry_date.grid(row=2, column=1, padx=10)

        self.label_description.grid(row=3, column=0, sticky=tk.W)
        self.entry_description.grid(row=3, column=1, padx=10)

        self.label_categories.grid(row=4, column=0, sticky=tk.W)
        self.entry_categories.grid(row=4, column=1, padx=10)

        # Place other labels and entry fields similarly

        self.button_record.grid(row=5, column=0, columnspan=2)
        self.button_edit.grid(row=6, column=0, columnspan=2)
        self.button_delete.grid(row=7, column=0, columnspan=2)
        self.button_view_expenses.grid(row=8, column=0, columnspan=2)
        self.button_view_total_spending.grid(row=9, column=0, columnspan=2)
        self.button_view_spending_by_category.grid(row=10, column=0, columnspan=2)
        self.button_generate_chart.grid(row=11, column=0, columnspan=2)
        self.button_get_expenses_by_category.grid(row=12, column=0, columnspan=2)
        self.button_calculate_average_spending_by_category.grid(row=13, column=0, columnspan=2)
        self.button_get_top_spending_category.grid(row=14, column=0, columnspan=2)
        self.button_calculate_spending_trend.grid(row=15, column=0, columnspan=2)
        self.button_export_expenses_to_csv.grid(row=16, column=0, columnspan=2)
        self.button_import_expenses_from_csv.grid(row=17, column=0, columnspan=2)
        
        # Place other buttons

        self.result_text.grid(row=18, column=0, columnspan=2, padx=10, pady=10)

    def record_expense(self):
        # Get input from user
        amount = float(self.entry_amount.get())
        date_str = self.entry_date.get()
        date = datetime.strptime(date_str, "%Y-%m-%d")
        description = self.entry_description.get()
        categories = self.entry_categories.get().split(",")

        # Call expense_manager.record_expense with the input
        self.expense_tracker.record_expense(amount, date, description, categories)
        self.result_text.insert(tk.END, "Expense recorded successfully.\n")

    def edit_expense(self):
        # Get selected expense for editing
        expenses = self.expense_tracker.view_expenses()
        selected_expense = self.select_expense("Select an expense to edit:", expenses)
        if selected_expense is not None:
            new_amount = float(input("New amount: "))
            new_date_str = input("New date (YYYY-MM-DD): ")
            new_date = datetime.strptime(new_date_str, "%Y-%m-%d")
            new_description = self.entry_description.get()
            new_categories = self.entry_categories.get().split(",")

            self.expense_tracker.edit_expense(selected_expense, new_amount, new_date, new_description, new_categories)
            self.result_text.insert(tk.END, "Expense edited successfully.\n")


    def delete_expense(self):
        # Get selected expense for deletion
        expenses = self.expense_tracker.view_expenses()
        selected_expense = self.select_expense("Select an expense to delete:", expenses)
        if selected_expense is not None:
            self.expense_tracker.delete_expense(selected_expense)
            self.result_text.insert(tk.END, "Expense deleted.\n")

    def view_expenses(self):
        # Call view_expenses method and display in result_text
        expenses = self.expense_tracker.view_expenses()
        self.result_text.delete(1.0, tk.END)
        for expense in expenses:
            self.result_text.insert(tk.END, str(expense.to_dict()) + "\n")

    def select_expense(self, prompt, expenses):
        print(prompt)
        for idx, expense in enumerate(expenses):
            print(f"{idx + 1}. {expense.to_dict()}")
        selected_idx = int(input("Enter the index of the expense: ")) - 1
        if 0 <= selected_idx < len(expenses):
            return expenses[selected_idx]
        else:
            print("Invalid index. Please try again.")
            return None

    def view_total_spending(self):
        total_spending = self.expense_tracker.view_total_spending()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Total spending: {total_spending:.2f}\n")

    def view_spending_by_category(self):
        spending_by_category = self.expense_tracker.view_spending_by_category()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Spending by category:\n")
        for category, amount in spending_by_category.items():
            self.result_text.insert(tk.END, f"{category}: {amount:.2f}\n")

    def generate_chart(self):
        self.expense_tracker.generate_chart()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Chart generated.\n")

    def get_expenses_by_category(self):
        category = input("Enter category: ")
        expenses = self.expense_tracker.get_expenses_by_category(category)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Expenses for category '{category}':\n")
        for expense in expenses:
            self.result_text.insert(tk.END, f"{expense.to_dict()}\n")

    def calculate_average_spending_by_category(self):
        category = input("Enter category: ")
        average_spending = self.expense_tracker.calculate_average_spending_by_category(category)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Average spending for category '{category}': {average_spending:.2f}\n")

    def get_top_spending_category(self):
        top_spending_category = self.expense_tracker.get_top_spending_category()
        self.result_text.delete(1.0, tk.END)
        if top_spending_category:
            self.result_text.insert(tk.END, f"Top spending category: {top_spending_category}\n")
        else:
            self.result_text.insert(tk.END, "No expenses recorded.\n")

    def calculate_spending_trend(self):
        spending_trend = self.expense_tracker.calculate_spending_trend()
        self.result_text.delete(1.0, tk.END)
        if spending_trend:
            self.result_text.insert(tk.END, "Spending trend:\n")
            for category, trend in spending_trend.items():
                self.result_text.insert(tk.END, f"{category}: {trend}\n")
        else:
            self.result_text.insert(tk.END, "No expenses recorded.\n")

    def export_expenses_to_csv(self):
        filename = input("Enter filename: ")
        expenses_to_export = self.expense_tracker.view_expenses()
        self.expense_io.export_expenses_to_csv(filename, expenses_to_export)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Expenses exported to {filename}\n")

    def import_expenses_from_csv(self):
        filename = '/Users/moukthika/Documents/my-projects/gpt-engineer/projects/expense2/workspace/expenses1.csv'
        expenses_imported = self.expense_io.import_expenses_from_csv(filename)
        for expense in expenses_imported:
            self.expense_tracker.record_expense(expense.amount, expense.date, expense.description, expense.categories)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Expenses imported successfully from {filename}\n")


    
def main():
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
