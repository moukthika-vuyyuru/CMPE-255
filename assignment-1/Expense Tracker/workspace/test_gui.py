import unittest
import tkinter as tk
from gui import ExpenseTrackerGUI

class TestExpenseTrackerGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = ExpenseTrackerGUI(self.root)
        self.app.root.withdraw()  # Hide the main window during tests

    def tearDown(self):
        self.root.destroy()

    def simulate_input(self, *inputs):
        input_queue = list(inputs)

        def simulated_input(prompt=""):
            return input_queue.pop(0)

        self.app.entry_amount.insert(0, "100")
        self.app.entry_date.insert(0, "2023-08-29")
        self.app.entry_description.insert(0, "Test Expense")
        self.app.entry_categories.insert(0, "Food, Groceries")

        builtin_input = __builtins__.input
        __builtins__.input = simulated_input

    def test_record_expense(self):
        self.simulate_input()
        self.app.record_expense()
        result = self.app.result_text.get("1.0", tk.END)
        self.assertIn("Expense recorded successfully.", result)

    def test_view_total_spending(self):
        self.app.view_total_spending()
        result = self.app.result_text.get("1.0", tk.END)
        self.assertIn("Total spending:", result)

    def test_view_spending_by_category(self):
        self.app.view_spending_by_category()
        result = self.app.result_text.get("1.0", tk.END)
        self.assertIn("Spending by category:", result)

    def test_generate_chart(self):
        self.app.generate_chart()
        result = self.app.result_text.get("1.0", tk.END)
        self.assertIn("Chart generated.", result)

    def test_get_expenses_by_category(self):
        self.simulate_input("Food")
        self.app.get_expenses_by_category()
        result = self.app.result_text.get("1.0", tk.END)
        self.assertIn("Expenses for category 'Food':", result)

    def test_calculate_average_spending_by_category(self):
        self.simulate_input("Groceries")
        self.app.calculate_average_spending_by_category()
        result = self.app.result_text.get("1.0", tk.END)
        self.assertIn("Average spending for category 'Groceries':", result)

    def test_get_top_spending_category(self):
        self.app.get_top_spending_category()
        result = self.app.result_text.get("1.0", tk.END)
        self.assertIn("Top spending category:", result)

    def test_calculate_spending_trend(self):
        self.app.calculate_spending_trend()
        result = self.app.result_text.get("1.0", tk.END)
        self.assertIn("Spending trend:", result)

    def test_export_import_expenses(self):
        filename = "test_expenses.csv"
        self.simulate_input(filename)
        self.app.export_expenses_to_csv()
        self.app.import_expenses_from_csv()
        result = self.app.result_text.get("1.0", tk.END)
        self.assertIn(f"Expenses imported successfully from {filename}", result)

if __name__ == "__main__":
    unittest.main()
