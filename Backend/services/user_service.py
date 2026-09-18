from sqlalchemy.orm import Session

from Backend.repositories.user_repository import (
    create_user,
    get_user,
    get_user_by_email,
    get_all_users,
)
from Backend.security import hash_password, verify_password

def register_customer(db: Session, name: str, email: str, password: str, is_admin: bool = False):
    return create_user(db, name, email, hash_password(password), is_admin)

def search_customer(db: Session, user_id: int):
    return get_user(db, user_id)

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user is None or not verify_password(password, user.password_hash):
        return None
    return user

def list_all_customers(db: Session):
    return get_all_users(db)

