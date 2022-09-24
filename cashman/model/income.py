from marshmallow import post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType

"""
Main Income class to be used for schema
Takes in a Transaction object that matches with the description/amount/type
"""
class Income(Transaction):
    def __init__(self, description, amount):
        super(Income, self).__init__(description, amount, TransactionType.INCOME)
    def __repr__(self):
        return '<Income(name={self.description!r}>'.format(self=self)

"""
Schema for income
Loads up a Transaction object
"""
class IncomeSchema(TransactionSchema):
    @post_load
    def make_income(self, data, **kwargs):
        return Income(**data)