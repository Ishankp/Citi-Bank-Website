from fastapi import APIRouter, HTTPException

from Backend.schemas.account import Account
from Backend.services.account_service import get_account_by_id, get_all_accounts

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.get("/", response_model=list[Account])
def get_accounts():
    return get_all_accounts()


@router.get("/{account_id}", response_model=Account)
def get_account(account_id: int):
    account = get_account_by_id(account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")

    return account
