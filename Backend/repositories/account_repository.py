from Backend.data.accounts import accounts

#Creates account based on userID and account type
#Returns the newly created account
def create_account(user_id:int,account_type:str):
    new_account_id = max(account["account_id"] for account in accounts) + 1
    new_account = {
        "account_id": new_account_id,
        "user_id": user_id,
        "balance": 0.0,
        "account_type": account_type,
        "created_at": "2023-01-15T10:30:00Z",
    }
    accounts.append(new_account)
    return new_account

#There is a one-to-many relationship between users and accounts, so we can have multiple accounts for a single user.
#Therefore, we will return a list of accounts for a given user_id
def get_all_accounts(user_id: int):
    return [account for account in accounts if account["user_id"] == user_id]

#Function that gets a specific account based on account_id
#Returns the account if found, None if not found
def get_account(account_id: int):
    account = next((account for account in accounts if account["account_id"] == account_id), None)
    return account

#Function that changes the balance of the account given account_id
#Returns the updated account if successful, None if account_id not found
def change_balance(account_id: int, new_balance: float):
    account = next((account for account in accounts if account["account_id"] == account_id), None)
    if account:
        account["balance"] = new_balance
        return account
    return None

#Function that views the balance of the account given account_id
#Returns the balance of account if successful, None if account_id not found
def view_balance(account_id: int):
    account = next((account for account in accounts if account["account_id"] == account_id), None)
    if account:
        return account["balance"]
    return None