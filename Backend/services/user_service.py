from sqlalchemy.orm import Session

from Backend.repositories.user_repository import (
    create_user,
    get_user
)

def register_customer(db: Session, name: str, email: str):
    return create_user(db, name, email)

def search_customer(db: Session, user_id: int):
    return get_user(db, user_id)

