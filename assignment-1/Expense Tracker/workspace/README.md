Based on the requirements, here are the core classes, functions, and methods that will be necessary for the Expense Tracker application:

1. Expense:
   - Properties:
     - amount: float
     - date: datetime
     - description: str
     - categories: List[str]
   - Methods:
     - __init__(amount: float, date: datetime, description: str, categories: List[str])
     - to_dict() -> Dict[str, Any]

2. ExpenseTracker:
   - Properties:
     - expenses: List[Expense]
   - Methods:
     - __init__()
     - add_expense(expense: Expense)
     - get_expenses() -> List[Expense]
     - get_total_spending() -> float
     - get_spending_by_category() -> Dict[str, float]
     - edit_expense(expense: Expense, new_amount: float, new_date: datetime, new_description: str, new_categories: List[str])
     - delete_expense(expense: Expense)

3. ExpenseChart:
   - Properties:
     - expense_tracker: ExpenseTracker
   - Methods:
     - __init__(expense_tracker: ExpenseTracker)
     - generate_pie_chart() -> None

4. ExpenseManager:
   - Properties:
     - expense_tracker: ExpenseTracker
     - expense_chart: ExpenseChart
   - Methods:
     - __init__(expense_tracker: ExpenseTracker, expense_chart: ExpenseChart)
     - record_expense(amount: float, date: datetime, description: str, categories: List[str])
     - edit_expense(expense: Expense, new_amount: float, new_date: datetime, new_description: str, new_categories: List[str])
     - delete_expense(expense: Expense)
     - view_expenses() -> List[Expense]
     - view_total_spending() -> float
     - view_spending_by_category() -> Dict[str, float]
     - generate_chart() -> None

5. main:
   - Instantiate ExpenseManager and run the application

Now let's proceed with creating the necessary files and implementing the code.

**expense.py**
