import pytest
from unittest.mock import mock_open, patch
from services.storage_service import load_transactions, calculate_totals
from models.transaction import Transaction

# test loading transactions from CSV
def test_load_transactions_returns_list_of_transactions():
    # arrange
    fake_cvs_data = (
        "type,title,amount,category,date,description\n"
        "Income,Salary,5000.00,Salary,03/10/2026,Monthly salary\n"
        "Expense,Dinner,100.00,Food,03/10/2026,Dinner at restaurant\n"
    )
    
    with patch("builtins.open", mock_open(read_data=fake_cvs_data)):
        # act
        result = load_transactions()

        # assert
        assert len(result) == 2
        assert isinstance(result[0], Transaction)
        assert result[0].transaction_type == "Income"
        assert result[1].transaction_type == "Expense"


# test calculating totals
def test_calculate_totals_sum_correctly():
    # arrange
    fake_csv = (
        "type,title,amount,category,date,description\n"
        "Income,Salary,5000.00,Salary,03/10/2026,Monthly salary\n"
        "Expense,Dinner,100.00,Food,03/10/2026,Dinner at restaurant\n"
        "Expense,Groceries,200.00,Food,03/11/2026,Weekly groceries\n"
    )

    with patch("builtins.open", mock_open(read_data=fake_csv)):
        # Act
        income, expense, balance = calculate_totals()

    # Assert
    assert income == 5000.00
    assert expense == 300.00
    assert balance == 4700.00


# test load_transactions() with empty CSV
def test_load_transactions_empty_file_returns_empty_list():
    # arrange
    fake_csv_data = ""

    with patch("builtins.open", mock_open(read_data=fake_csv_data)):
        # act
        result = load_transactions()

    # assert
    assert result == []


# test calculate_totals() with no transactions
def test_calculate_totals_no_transactions_returns_zeros():
    # arrange
    fake_csv_data = ""

    with patch("builtins.open", mock_open(read_data=fake_csv_data)):
        # act
        income, expense, balance = calculate_totals()

    # assert
    assert income == 0.00
    assert expense == 0.00
    assert balance == 0.00