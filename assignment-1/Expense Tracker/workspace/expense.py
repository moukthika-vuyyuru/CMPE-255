from typing import List, Dict, Any
from datetime import datetime

class Expense:
    def __init__(self, amount: float, date: datetime, description: str, categories: List[str]):
        self.amount = amount
        self.date = date
        self.description = description
        self.categories = categories

    def to_dict(self) -> Dict[str, Any]:
        return {
            'amount': self.amount,
            'date': self.date,
            'description': self.description,
            'categories': self.categories
        }
