from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Backend.database import get_db
from Backend.schemas.account import UserCreate, Users
from Backend.services.user_service import register_customer, search_customer

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.post("", response_model=Users, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return register_customer(db, user_data.name, user_data.email)


@router.get("/{user_id}", response_model=Users)
def get_user_details(user_id: int, db: Session = Depends(get_db)):
    user = search_customer(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user
