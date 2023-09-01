from expense_tracker import ExpenseTracker
from expense_chart import ExpenseChart
from expense import Expense
from datetime import datetime

# This class is responsible for managing expenses
class ExpenseManager:
    def __init__(self, expense_tracker: ExpenseTracker, expense_chart: ExpenseChart):
        self.expense_tracker = expense_tracker
        self.expense_chart = expense_chart

    def record_expense(self, amount: float, date: datetime, description: str, categories: list[str]):
        # create an Expense object
        expense = Expense(amount, date, description, categories)
        self.expense_tracker.add_expense(expense)

    # edit an expense
    def edit_expense(self, expense: Expense, new_amount: float, new_date: datetime, new_description: str, new_categories: list[str]):
        self.expense_tracker.edit_expense(expense, new_amount, new_date, new_description, new_categories)

    # delete an expense
    def delete_expense(self, expense: Expense):
        self.expense_tracker.delete_expense(expense)

    # view expenses
    def view_expenses(self) -> list[Expense]:
        return self.expense_tracker.get_expenses()

    # view total spending
    def view_total_spending(self) -> float:
        return self.expense_tracker.get_total_spending()

    # view spending by category
    def view_spending_by_category(self) -> dict[str, float]:
        return self.expense_tracker.get_spending_by_category()

    # generate pie chart
    def generate_chart(self):
        self.expense_chart.generate_pie_chart()

    # get expenses by category
    def get_expenses_by_category(self, category: str) -> list[Expense]:
        return self.expense_tracker.get_expenses_by_category(category)
    
    # calculate average spending by category
    def calculate_average_spending_by_category(self, category: str):
        expenses = self.expense_tracker.get_expenses_by_category(category)
        if expenses:
            total_spending = sum(expense.amount for expense in expenses)
            average_spending = total_spending / len(expenses)
            return average_spending
        else:
            return 0.0
    
    # get top spending category
    def get_top_spending_category(self):   
        spending_by_category = self.expense_tracker.get_spending_by_category()
        if spending_by_category:
            return max(spending_by_category, key=spending_by_category.get)
        else:
            return None
        
    # calculate spending trend
    def calculate_spending_trend(self):
        spending_by_category = self.expense_tracker.get_spending_by_category()
        if spending_by_category:
            spending_trend = {}
            for expense in self.expense_tracker.get_expenses():
                for category in expense.categories:
                    if category not in spending_trend:
                        spending_trend[category] = {}
                    month = expense.date.strftime("%Y-%m")
                    if month not in spending_trend[category]:
                        spending_trend[category][month] = 0
                    spending_trend[category][month] += expense.amount
            return spending_trend
        else:
            return None
        
    # calculate spending trend by month
    def calculate_spending_trend_by_month(self):
        spending_trend = self.calculate_spending_trend()
        if spending_trend:
            return list(spending_trend.values())
        else:
            return None
