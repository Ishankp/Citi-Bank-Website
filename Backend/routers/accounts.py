from fastapi import APIRouter, HTTPException, status

from Backend.schemas.account import Account, AccountCreate, MoneyRequest, Transactions
from Backend.services.account_service import (
    customer_deposit,
    customer_withdraw,
    find_specific_customer_account,
    register_customer_account,
)
from Backend.services.transaction_service import customer_create_transaction, customer_view_transactions

router = APIRouter(prefix="/api/accounts", tags=["Accounts"])


@router.post("", response_model=Account, status_code=status.HTTP_201_CREATED)
def create_account(account_data: AccountCreate):
    return register_customer_account(account_data.user_id, account_data.account_type)


@router.get("/{account_id}", response_model=Account)
def get_account_details(account_id: int):
    account = find_specific_customer_account(account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")

    return account


@router.post("/{account_id}/deposit", response_model=Account)
def deposit_money(account_id: int, request: MoneyRequest):
    try:
        account = customer_deposit(account_id, request.amount)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    customer_create_transaction(account_id, request.amount, "deposit")
    return account


@router.post("/{account_id}/withdraw", response_model=Account)
def withdraw_money(account_id: int, request: MoneyRequest):
    try:
        account = customer_withdraw(account_id, request.amount)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    customer_create_transaction(account_id, request.amount, "withdrawal")
    return account


@router.get("/{account_id}/transactions", response_model=list[Transactions])
def get_transaction_history(account_id: int):
    if find_specific_customer_account(account_id) is None:
        raise HTTPException(status_code=404, detail="Account not found")

    return customer_view_transactions(account_id)
