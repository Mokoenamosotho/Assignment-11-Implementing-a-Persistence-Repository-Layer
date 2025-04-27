import unittest
from factories.repository_factory import RepositoryFactory
from repositories.inmemory.in_memory_database_repository import InMemoryDatabaseRepository

class TestRepositoryFactory(unittest.TestCase):
    def test_get_in_memory_database_repository(self):
        repo = RepositoryFactory.get_database_repository("MEMORY")
        self.assertIsInstance(repo, InMemoryDatabaseRepository)

    def test_invalid_storage_type(self):
        with self.assertRaises(ValueError):
            RepositoryFactory.get_database_repository("INVALID")

    def test_unimplemented_storage_type(self):
        with self.assertRaises(NotImplementedError):
            RepositoryFactory.get_database_repository("DATABASE")

if __name__ == "__main__":
    unittest.main()