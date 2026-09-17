from sqlalchemy.orm import Session

from Backend.repositories.account_repository import (
    get_account,
    create_account,
    change_balance,
    view_balance,
    get_all_accounts
)



def register_customer_account(db: Session, user_id: int, account_type: str):
    return create_account(db, user_id, account_type)

def find_specific_customer_account(db: Session, account_id: int):
    return get_account(db, account_id)

def find_all_customer_accounts(db: Session, user_id: int):
    return get_all_accounts(db, user_id)


def view_customer_balance(db: Session, account_id: int):
    return view_balance(db, account_id)

def customer_deposit(db: Session, account_id: int, amount: float):
    curr_balance = view_balance(db, account_id)
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")

    if (curr_balance is None):
        raise ValueError("Account not found.")
    return change_balance(db, account_id, amount + curr_balance)

def customer_withdraw(db: Session, account_id: int, amount: float):
    curr_balance = view_balance(db, account_id)
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")

    if (curr_balance is None):
        raise ValueError("Account not found.")
    if (curr_balance < amount):
        raise ValueError("Insufficient funds.")
    return change_balance(account_id, curr_balance-amount)


