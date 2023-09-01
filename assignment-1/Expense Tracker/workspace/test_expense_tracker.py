# write unit tests for the ExpenseTracker class
# Path: tests/test_expense_tracker.py
import unittest
from datetime import datetime
from expense import Expense
from expense_tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.expense_tracker = ExpenseTracker()
        self.expense1 = Expense(10.50, datetime.now(), "Lunch", ["Food"])
        self.expense2 = Expense(25.00, datetime.now(), "Movie ticket", ["Entertainment"])
        self.expense3 = Expense(50.00, datetime.now(), "Groceries", ["Food"])
        self.expense4 = Expense(15.00, datetime.now(), "Coffee", ["Food", "Beverages"])
        self.expense_tracker.add_expense(self.expense1)
        self.expense_tracker.add_expense(self.expense2)
        self.expense_tracker.add_expense(self.expense3)
        self.expense_tracker.add_expense(self.expense4)

    def test_get_expenses(self):
        self.assertEqual(self.expense_tracker.get_expenses(), [self.expense1, self.expense2, self.expense3, self.expense4])
        
    def test_get_total_spending(self):
        self.assertEqual(self.expense_tracker.get_total_spending(), 100.50)

    def test_get_spending_by_category(self):
        self.assertEqual(self.expense_tracker.get_spending_by_category(), {"Food": 75.50, "Entertainment": 25.00, "Beverages": 15.00})

    def test_edit_expense(self):
        self.expense_tracker.edit_expense(self.expense1, 15.50, datetime.now(), "Lunch", ["Food"])
        self.assertEqual(self.expense1.to_dict(), {'amount': 15.50, 'date': self.expense1.date, 'description': 'Lunch', 'categories': ['Food']})

    def test_delete_expense(self):
        self.expense_tracker.delete_expense(self.expense1)
        self.assertEqual(self.expense_tracker.get_expenses(), [self.expense2, self.expense3, self.expense4])

    def test_get_expenses_by_category(self):
        self.assertEqual(self.expense_tracker.get_expenses_by_category("Food"), [self.expense1, self.expense3, self.expense4])


if __name__ == "__main__":
    unittest.main()
    