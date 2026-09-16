from Backend.data.accounts import users


def create_user(name: str, email: str):
    new_user_id = max(user["user_id"] for user in users) + 1
    new_user = {
        "user_id": new_user_id,
        "name": name,
        "email": email,
        "created_at": "2023-01-15T10:30:00Z",
    }
    users.append(new_user)
    return new_user

def get_user(user_id: int):
    return next((user for user in users if user["user_id"] == user_id), None)
