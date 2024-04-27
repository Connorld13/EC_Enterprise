class InMemoryDB:
    def __init__(self):
        self.data = {}
        self.transaction_active = False
        self.transaction_data = {}

    def begin_transaction(self):
        if self.transaction_active:
            raise Exception("Transaction already in progress")
        self.transaction_active = True
        self.transaction_data = {}

    def put(self, key, value):
        if not self.transaction_active:
            raise Exception("No transaction in progress. Call begin_transaction() first.")
        self.transaction_data[key] = value

    def get(self, key):
        if self.transaction_active and key in self.transaction_data:
            return self.transaction_data[key]
        return self.data.get(key, None)

    def commit(self):
        if not self.transaction_active:
            raise Exception("No transaction to commit.")
        self.data.update(self.transaction_data)
        self.transaction_active = False
        self.transaction_data = {}

    def rollback(self):
        if not self.transaction_active:
            raise Exception("No transaction to rollback.")
        self.transaction_active = False
        self.transaction_data = {}

# Example usage:
db = InMemoryDB()

print(db.get("A"))  # Should return None since 'A' is not set

try:
    db.put("A", 5)  # Should raise an exception because no transaction is active
except Exception as e:
    print(e)  # Expected error message about no transaction

db.begin_transaction()  # Starting a transaction
db.put("A", 5)  # Putting 'A' as 5 within the transaction
print(db.get("A"))  # Should return 5 because 'A' is set in the transaction

db.put("A", 6)  # Updating 'A' to 6 within the same transaction
db.commit()  # Committing the transaction

print(db.get("A"))  # Should return 6 as the last committed value

try:
    db.commit()  # Should raise an error because no transaction is currently active
except Exception as e:
    print(e)  # Expected error message about no transaction to commit

try:
    db.rollback()  # Should also raise an error because no transaction is active
except Exception as e:
    print(e)  # Expected error message about no transaction to rollback
