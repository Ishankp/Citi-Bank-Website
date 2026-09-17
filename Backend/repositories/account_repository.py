from sqlalchemy.orm import Session

from Backend.models import Account

#Creates account based on userID and account type
#Returns the newly created account
def create_account(db: Session, user_id: int, account_type: str):
    new_account = Account(user_id=user_id, account_type=account_type, balance=0.0)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

#There is a one-to-many relationship between users and accounts, so we can have multiple accounts for a single user.
#Therefore, we will return a list of accounts for a given user_id
def get_all_accounts(db: Session, user_id: int):
    return db.query(Account).filter(Account.user_id == user_id).all()

#Function that gets a specific account based on account_id
#Returns the account if found, None if not found
def get_account(db: Session, account_id: int):
    return db.query(Account).filter(Account.account_id == account_id).first()

#Function that changes the balance of the account given account_id
#Returns the updated account if successful, None if account_id not found
def change_balance(db: Session, account_id: int, new_balance: float):
    account = get_account(db, account_id)
    if account:
        account.balance = new_balance
        db.commit()
        db.refresh(account)
        return account
    return None

#Function that views the balance of the account given account_id
#Returns the balance of account if successful, None if account_id not found
def view_balance(db: Session, account_id: int):
    account = get_account(db, account_id)
    if account:
        return account.balance
    return None
    if account:
        return account["balance"]
    return None