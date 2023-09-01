from datetime import datetime
from typing import List
from expense import Expense

# This class is responsible for managing expenses
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    # add an expense
    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    # view expenses
    def get_expenses(self) -> List[Expense]:
        return self.expenses

    # view total spending
    def get_total_spending(self) -> float:
        return sum(expense.amount for expense in self.expenses)

    # view spending by category
    def get_spending_by_category(self) -> dict[str, float]:
        spending_by_category = {}
        for expense in self.expenses:
            for category in expense.categories:
                spending_by_category[category] = spending_by_category.get(category, 0) + expense.amount
        return spending_by_category

    # edit an expense
    def edit_expense(self, expense: Expense, new_amount: float, new_date: datetime, new_description: str, new_categories: list[str]):
        expense.amount = new_amount
        expense.date = new_date
        expense.description = new_description
        expense.categories = new_categories

    # delete an expense
    def delete_expense(self, expense: Expense):
        self.expenses.remove(expense)
    
    # get expenses by Category
    def get_expenses_by_category(self, category: str) -> List[Expense]:
        return [expense for expense in self.expenses if category in expense.categories]
