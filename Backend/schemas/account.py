from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class Account(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    account_id: int
    user_id: int
    balance: float
    account_type: str
    created_at: datetime


class AccountCreate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: int = Field(alias="userId")
    account_type: str = Field(alias="accountType")


class MoneyRequest(BaseModel):
    amount: float

class Users(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    name: str
    email: str
    is_admin: bool
    created_at: datetime

class UserCreate(BaseModel):
    name: str
    email: str
    password: str = Field(min_length=6)
    is_admin: bool = False

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: Users

class Transactions(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    txn_id: int
    account_id: int
    txn_type: str
    amount: float
    created_at: datetime

