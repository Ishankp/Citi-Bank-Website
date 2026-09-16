from Backend.data.accounts import transactions


def view_transactions(account_id: int):
    return [txn for txn in transactions if txn["account_id"] == account_id]


def create_transaction(account_id: int, amount: float, txn_type: str):
    new_txn_id = max(txn["txn_id"] for txn in transactions) + 1
    new_transaction = {
        "txn_id": new_txn_id,
        "account_id": account_id,
        "txn_type": txn_type,
        "amount": amount,
        "created_at": "2023-01-15T10:30:00Z",
    }
    transactions.append(new_transaction)
    return new_transaction
