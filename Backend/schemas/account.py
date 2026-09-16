from pydantic import BaseModel


class Account(BaseModel):
    account_id: int
    user_id: int
    balance: float
    account_type: str
    created_at: str

class Users(BaseModel):
    user_id: int
    name: str
    email: str
    created_at: str

class Transactions(BaseModel):
    txn_id: int
    account_id: int
    txn_type: str
    amount: float
    created_at: str
