from Backend.repositories.transaction_repository import (
    view_transactions,
    create_transaction
)

def customer_view_transactions(account_id: int):
    return view_transactions(account_id)

def customer_create_transaction(account_id: int, amount: float, txn_type: str):
    return create_transaction(account_id, amount, txn_type)