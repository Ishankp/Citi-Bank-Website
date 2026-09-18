from sqlalchemy.orm import Session

from Backend.models import User


def create_user(db: Session, name: str, email: str, password_hash: str, is_admin: bool = False):
    new_user = User(name=name, email=email, password_hash=password_hash, is_admin=is_admin)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_all_users(db: Session):
    return db.query(User).all()
