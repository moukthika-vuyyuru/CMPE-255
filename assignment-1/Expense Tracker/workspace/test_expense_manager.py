# Write unit tests for the ExpenseManager class
# Path: test_expense_manager.py (in the tests folder)
import unittest
from datetime import datetime
from expense import Expense
from expense_tracker import ExpenseTracker
from expense_chart import ExpenseChart
from expense_manager import ExpenseManager

class TestExpenseManager(unittest.TestCase):
    def setUp(self) -> None:
        self.expense_tracker = ExpenseTracker()
        self.expense_chart = ExpenseChart(self.expense_tracker) 
        self.expense_manager = ExpenseManager(self.expense_tracker, self.expense_chart)
        self.expense1 = Expense(10.50, datetime.now(), "Lunch", ["Food"])
        self.expense2 = Expense(25.00, datetime.now(), "Movie ticket", ["Entertainment"])
        self.expense3 = Expense(50.00, datetime.now(), "Groceries", ["Food"])
        self.expense4 = Expense(15.00, datetime.now(), "Coffee", ["Food", "Beverages"])
        self.expense_tracker.add_expense(self.expense1)
        self.expense_tracker.add_expense(self.expense2)
        self.expense_tracker.add_expense(self.expense3)
        self.expense_tracker.add_expense(self.expense4)

    def test_record_expense(self):
        self.expense_manager.record_expense(10.50,datetime.now(), "Lunch", ["Food"])
        self.assertEqual(len(self.expense_tracker.expenses), 5)

    def test_view_expenses(self):
        self.assertEqual(len(self.expense_manager.view_expenses()), 4)

    def test_view_total_spending(self):
        self.assertEqual(self.expense_manager.view_total_spending(), 100.50)

    def test_view_spending_by_category(self):
        self.assertEqual(self.expense_manager.view_spending_by_category(), {'Food': 75.5, 'Entertainment': 25.0, 'Beverages': 15.0})

    def test_edit_expense(self):
        self.expense_manager.edit_expense(self.expense1, 10.50, datetime.now(), "Lunch", ["Food"])
        self.assertEqual(self.expense1.amount, 10.50)
        self.assertEqual(self.expense1.description, "Lunch")
        self.assertEqual(self.expense1.categories, ["Food"])

    def test_delete_expense(self):
        self.expense_manager.delete_expense(self.expense1)
        self.assertEqual(len(self.expense_tracker.expenses), 3)
        
    def test_get_expenses_by_category(self):
        self.assertEqual(len(self.expense_manager.get_expenses_by_category("Food")), 3)

    def test_calculate_average_spending_by_category(self):
        self.assertEqual(self.expense_manager.calculate_average_spending_by_category("Food"), 25.166666666666668)

    def test_get_top_spending_category(self):
        self.assertEqual(self.expense_manager.get_top_spending_category(), "Food")

if __name__ == "__main__":
    unittest.main()
