import unittest
from InMemoryDB import InMemoryDB

class TestInMemoryDB(unittest.TestCase):

    def setUp(self):
        """Initialize a fresh database instance for each test."""
        self.db = InMemoryDB()

    def test_get_nonexistent(self):
        """Test getting a non-existent key should return None."""
        self.assertIsNone(self.db.get("A"))

    def test_put_without_transaction(self):
        """Test that put without a transaction raises an exception."""
        with self.assertRaises(Exception) as context:
            self.db.put("A", 5)
        self.assertIn("No transaction in progress", str(context.exception))

    def test_transaction_commit(self):
        """Test putting and committing a key-value pair."""
        self.db.begin_transaction()
        self.db.put("A", 5)
        self.db.commit()
        self.assertEqual(self.db.get("A"), 5)

    def test_transaction_rollback(self):
        """Test putting a key-value pair and then rolling it back."""
        self.db.begin_transaction()
        self.db.put("A", 5)
        self.db.rollback()
        self.assertIsNone(self.db.get("A"))

    def test_errors_on_commit_without_transaction(self):
        """Test committing without an active transaction raises an exception."""
        with self.assertRaises(Exception) as context:
            self.db.commit()
        self.assertIn("No transaction to commit", str(context.exception))

    def test_errors_on_rollback_without_transaction(self):
        """Test rolling back without an active transaction raises an exception."""
        with self.assertRaises(Exception) as context:
            self.db.rollback()
        self.assertIn("No transaction to rollback", str(context.exception))

if __name__ == '__main__':
    unittest.main()
