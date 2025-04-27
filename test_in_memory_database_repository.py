import unittest
from repositories.inmemory.in_memory_database_repository import InMemoryDatabaseRepository, Database

class TestInMemoryDatabaseRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryDatabaseRepository()

    def test_save_and_find_by_id(self):
        db = Database(id="1", name="TestDB")
        self.repo.save(db, db.id)
        retrieved = self.repo.find_by_id("1")
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.name, "TestDB")

    def test_delete_by_id(self):
        db = Database(id="2", name="DeleteDB")
        self.repo.save(db, db.id)
        self.repo.delete_by_id("2")
        self.assertIsNone(self.repo.find_by_id("2"))

    def test_find_all(self):
        db1 = Database(id="3", name="DB1")
        db2 = Database(id="4", name="DB2")
        self.repo.save(db1, db1.id)
        self.repo.save(db2, db2.id)
        all_dbs = self.repo.find_all()
        self.assertEqual(len(all_dbs), 2)
        self.assertIn("3", all_dbs)
        self.assertIn("4", all_dbs)

if __name__ == "__main__":
    unittest.main()