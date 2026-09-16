from pydantic import BaseModel, ConfigDict, Field


class Account(BaseModel):
    account_id: int
    user_id: int
    balance: float
    account_type: str
    created_at: str


class AccountCreate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: int = Field(alias="userId")
    account_type: str = Field(alias="accountType")


class MoneyRequest(BaseModel):
    amount: float

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
