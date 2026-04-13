from models.transaction import Transaction
from services.storage_service import append_transaction

def save_transaction(values):
    # convert transaction dict to list
    transaction_type = "Income" if values["radio_income"] else "Expense"

    # create a Transaction object from the form values
    transaction = Transaction(
        transaction_type=transaction_type,
        title=values["tx_title"],
        amount=values["amount"],
        category=values["category"],
        date=values["date"],
        description=values["description"],
    )

    # validate the transaction data
    errors = transaction.validations()
    if errors:
        return False, errors # return False and the list of errors if validation fails
    
    append_transaction(transaction)
    return True, None