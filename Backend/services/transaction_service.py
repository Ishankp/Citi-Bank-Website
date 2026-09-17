from sqlalchemy.orm import Session

from Backend.repositories.transaction_repository import (
    view_transactions,
    create_transaction
)

def customer_view_transactions(db: Session, account_id: int):
    return view_transactions(db, account_id)

def customer_create_transaction(db: Session, account_id: int, amount: float, txn_type: str):
    return create_transaction(db, account_id, amount, txn_type)