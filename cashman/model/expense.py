from marshmallow import post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType

"""
Main Expense class to be used for schema
Takes in a Transaction object that matches with the description/amount/type
"""
class Expense(Transaction):
    def __init__(self, description, amount):
        super(Expense, self).__init__(description, -abs(amount), TransactionType.EXPENSE)
    def __repr__(self):
        return '<Expense(name={self.description!r})'.format(self=self)

"""
Schema for expense
Loads up a Transaction object
"""
class ExpenseSchema(TransactionSchema):
    @post_load
    def make_expense(self, data, **kwargs):
        return Expense(**data)