from datetime import datetime
from expense_chart import ExpenseChart
from expense_manager import ExpenseManager
from expense_tracker import ExpenseTracker
from expense_io import ExpenseIO

def main():
    expense_tracker = ExpenseTracker()
    expense_chart = ExpenseChart(expense_tracker)
    expense_manager = ExpenseManager(expense_tracker, expense_chart)
    expense_io = ExpenseIO()

    # Example usage
    expense_manager.record_expense(10.50,datetime.now(), "Lunch", ["Food"])
    expense_manager.record_expense(25.00, datetime.now(), "Movie ticket", ["Entertainment"])
    expense_manager.record_expense(50.00, datetime.now(), "Groceries", ["Food"])
    expense_manager.record_expense(15.00, datetime.now(), "Coffee", ["Food", "Beverages"])

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Record expense")
        print("2. Edit expense")
        print("3. Delete expense")
        print("4. View expenses")
        print("5. View total spending")
        print("6. View spending by category")
        print("7. Generate chart")
        print("8. Export expenses to CSV")
        print("9. Import expenses from CSV")
        print("10. Data Analytics")
        print("11. Exit")
    

        choice = input("Enter your choice: ")

        if choice == "1":
            # Record expense
            user_name = input("Enter your name: ")
            amount = float(input("Amount: "))
            date_str = input("Date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, "%Y-%m-%d")
            description = input("Description: ")
            categories = input("Categories (comma-separated): ").split(",")
            expense_manager.record_expense(amount, date, description, categories)

        elif choice == "2":
            # Edit expense
            expenses = expense_manager.view_expenses()
            print("Select an expense to edit:")
            for idx, expense in enumerate(expenses):
                print(f"{idx+1}. {expense.to_dict()}")
            selected_idx = int(input("Enter the index of the expense to edit: ")) - 1
            if 0 <= selected_idx < len(expenses):
                selected_expense = expenses[selected_idx]

                # Obtain new expense details from user
                new_amount = float(input("New amount: "))
                new_date_str = input("New date (YYYY-MM-DD): ")
                new_date = datetime.strptime(new_date_str, "%Y-%m-%d")
                new_description = input("New description: ")
                new_categories = input("New categories (comma-separated): ").split(",")

                # Call edit_expense with new details
                expense_manager.edit_expense(selected_expense, new_amount, new_date, new_description, new_categories)
                print("Expense edited successfully.")
            else:
                print("Invalid index. Please try again.")


        elif choice == "3":
            # Delete expense
            expenses = expense_manager.view_expenses()
            print("Select an expense to delete:")
            for idx, expense in enumerate(expenses):
                print(f"{idx+1}. {expense.to_dict()}")
            selected_idx = int(input("Enter the index of the expense to delete: ")) - 1
            if 0 <= selected_idx < len(expenses):
                selected_expense = expenses[selected_idx]
                expense_manager.delete_expense(selected_expense)
                print("Expense deleted.")
            else:
                print("Invalid index. Please try again.")

        elif choice == "4":
            # View expenses
            expenses = expense_manager.view_expenses()
            for expense in expenses:
                print(expense.to_dict())

        elif choice == "5":
            # View total spending
            total_spending = expense_manager.view_total_spending()
            print("Total spending:", total_spending)

        elif choice == "6":
            # View spending by category
            spending_by_category = expense_manager.view_spending_by_category()
            print("Spending by category:", spending_by_category)

        elif choice == "7":
            # Generate chart
            expense_manager.generate_chart()
        
        elif choice == "8":
            # Export expenses to CSV
            expenses_to_export = expense_manager.view_expenses()
            expense_io.export_expenses_to_csv('expenses.csv', expenses_to_export)
            print("Expenses exported to expenses.csv")

        elif choice == "9":
            # Import expenses from CSV
            expenses_imported = expense_io.import_expenses_from_csv('expenses1.csv')
            for expense in expenses_imported:
                expense_manager.record_expense(expense.amount, expense.date, expense.description, expense.categories)
            print("Expenses imported successfully.")
        
        elif choice == "10":
            # Data Analytics
            print("Data Analytics Menu:\n")
            print("1. Calculate Average Spending by catrgory")
            print("2. Top Spending Categories")
            print("3. Spending Trends")
            print("4. Back to main menu")

            analytics_choice = input("Enter your choice: ")

            if analytics_choice == "1":
                # Calculate average spending by Category
                category = input("Enter category: ")
                average_spending = expense_manager.calculate_average_spending_by_category(category)
                print("Average spending:", average_spending)

            elif analytics_choice == "2":
                # Top spending categories
                top_spending_categories = expense_manager.get_top_spending_category()
                print("Top spending categories:", top_spending_categories)

            elif analytics_choice == "3":
                # Spending trends by month
                spending_trends = expense_manager.calculate_spending_trend()
                print("Spending trends:", spending_trends)

            elif analytics_choice == "4":
                # Back to main menu
                continue

        elif choice == "11":
            # Exit
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
