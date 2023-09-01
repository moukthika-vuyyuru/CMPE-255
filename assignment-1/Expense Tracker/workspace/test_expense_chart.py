# write unit tests for the ExpenseChart class
# Path: test_expense_chart.py (in the tests folder)
import unittest
from datetime import datetime
from expense import Expense
from expense_tracker import ExpenseTracker
from expense_chart import ExpenseChart
from expense_manager import ExpenseManager

class TestExpenseChart(unittest.TestCase):
    def setUp(self):
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

    def test_generate_pie_chart(self):
        self.assertEqual(self.expense_chart.generate_pie_chart(), None)

if __name__ == "__main__":
    unittest.main()
    