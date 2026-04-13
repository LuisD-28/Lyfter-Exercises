import pytest
from models.transaction import Transaction

# test input data validation
def test_transaction_validation():
    #arrange
    data = {
        "transaction_type": "Income",
        "title": "Salary",
        "amount": 5000,
        "category": "Salary",
        "date": "03/10/2026",
        "description": "Monthly salary"
    }

    t = Transaction(**data)

    #act
    errors = t.validations()

    #assert
    assert errors == []  # no validation errors expected
    assert t.amount == 5000.00


def test_transaction_empty_title():
    #arrange
    t = Transaction(
        transaction_type="Expense",
        title="   ",  # empty title
        amount=100,
        category="Food",
        date="03/10/2026",
        description="Groceries"
    )

    #act
    errors = t.validations()

    #assert
    assert "Title cannot be empty." in errors


def test_transaction_invalid_amount():
    #arrange
    t = Transaction(
        transaction_type="Expense",
        title="Dinner",
        amount="abc",  # invalid amount
        category="Food",
        date="03/10/2026",
        description="Dinner at restaurant"
    )

    #act
    errors = t.validations()

    #assert
    assert "Amount must be a number." in errors




def test_transaction_future_date():
    #arrange
    t = Transaction(
        transaction_type="Income",
        title="Freelance Project",
        amount=2000,
        category="Freelance",
        date="12/31/2099",  # future date
        description="Payment for freelance work"
    )

    #act
    errors = t.validations()

    #assert
    assert "Date cannot be in the future." in errors

