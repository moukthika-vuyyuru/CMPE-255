# write unit tests for Expense class
import unittest
from datetime import datetime
from expense import Expense

class TestExpense(unittest.TestCase):
    def setUp(self):
        self.expense = Expense(10.50, datetime.now(), "Lunch", ["Food"])

    def test_to_dict(self):
        self.assertEqual(self.expense.to_dict(), {'amount': 10.50, 'date': self.expense.date, 'description': 'Lunch', 'categories': ['Food']})

if __name__ == "__main__":
    unittest.main()