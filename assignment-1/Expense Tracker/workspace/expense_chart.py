from expense_tracker import ExpenseTracker
import matplotlib.pyplot as plt

# This class is responsible for generating pie charts
class ExpenseChart:
    def __init__(self, expense_tracker: ExpenseTracker):
        self.expense_tracker = expense_tracker

# generate pie chart
    def generate_pie_chart(self):
        spending_by_category = self.expense_tracker.get_spending_by_category()
        categories = list(spending_by_category.keys())
        amounts = list(spending_by_category.values())

        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()
