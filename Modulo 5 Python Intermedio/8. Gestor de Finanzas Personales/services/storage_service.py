from models.transaction import Transaction
import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_PATH = os.path.join(DATA_DIR, "transactions.csv")


def ensure_csv_exists():
    #create a csv file and add header if it doesn't exist
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.isfile(CSV_PATH):
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["type", "title", "amount", "category", "date", "description"])


def append_transaction(transaction: Transaction):
    ensure_csv_exists()
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(transaction.to_csv_row())


def load_transactions():
    ensure_csv_exists()

    transaction = []
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for row in reader:
            transaction.append(Transaction.from_csv_row(row))

    return transaction


def calculate_totals():
    transaction = load_transactions()

    total_income = sum(t.amount for t in transaction if t.transaction_type == "Income")
    total_expense = sum(t.amount for t in transaction if t.transaction_type == "Expense")
    balance = total_income - total_expense

    return total_income, total_expense, balance


# def load_transactions():
#     ensure_csv_exists()

#     rows = []
#     with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
#         reader = csv.reader(f)
#         next(reader, None)  # skip header
#         for row in reader:
#             rows.append(row)
    
#     return rows