from enum import Enum

"""
Transaction Type
Represents enumerators for transaction types inside income class
"""
class TransactionType(Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"