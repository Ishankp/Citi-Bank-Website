from Backend.repositories.user_repository import (
    create_user,
    get_user
)

def register_customer(name: str, email: str):
    return create_user(name, email)

def search_customer(user_id: int):
    return get_user(user_id)

