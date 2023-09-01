from datetime import datetime
from expense import Expense

# This class is responsible for importing and exporting expenses to and from a CSV file
class ExpenseIO:
    @staticmethod
    def export_expenses_from_csv(filename,expenses):
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["Amount", "Date", "Description", "Categories"])
            for expense in expenses:
                writer.writerow([expense.amount, expense.date, expense.description, expense.categories])

    @staticmethod
    def import_expenses_to_csv(filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            expenses = []
            for row in reader:
                amount = float(row[0])
                date = datetime.strptime(row[1], "%Y-%m-%d")
                description = row[2]
                categories = row[3].split(",")
                expense = Expense(amount, date, description, categories)
                expenses.append(expense)
            return expenses
        
