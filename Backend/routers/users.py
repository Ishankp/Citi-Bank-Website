from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Backend.database import get_db
from Backend.dependencies import get_current_user
from Backend.schemas.account import Account, UserCreate, Users
from Backend.services.account_service import find_all_customer_accounts
from Backend.services.user_service import register_customer, search_customer

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.post("", response_model=Users, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return register_customer(db, user_data.name, user_data.email, user_data.password, user_data.is_admin)


@router.get("/{user_id}", response_model=Users)
def get_user_details(user_id: int, db: Session = Depends(get_db)):
    user = search_customer(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.get("/{user_id}/accounts", response_model=list[Account])
def get_user_accounts(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if search_customer(db, user_id) is None:
        raise HTTPException(status_code=404, detail="User not found")

    if current_user.user_id != user_id and not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to view these accounts")

    return find_all_customer_accounts(db, user_id)
