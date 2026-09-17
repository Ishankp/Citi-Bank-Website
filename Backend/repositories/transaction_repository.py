from sqlalchemy.orm import Session

from Backend.models import Transaction


def view_transactions(db: Session, account_id: int):
    return db.query(Transaction).filter(Transaction.account_id == account_id).all()


def create_transaction(db: Session, account_id: int, amount: float, txn_type: str):
    new_transaction = Transaction(account_id=account_id, amount=amount, txn_type=txn_type)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction
