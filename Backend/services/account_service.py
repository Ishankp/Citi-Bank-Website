from Backend.repositories.account_repository import (
    find_account_by_id,
    find_all_accounts,
)


def get_all_accounts():
    return find_all_accounts()


def get_account_by_id(account_id: int):
    return find_account_by_id(account_id)
