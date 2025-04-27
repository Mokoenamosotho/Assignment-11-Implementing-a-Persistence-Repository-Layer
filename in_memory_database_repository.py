from repositories.inmemory.in_memory_repository import InMemoryRepository

class Database:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

class InMemoryDatabaseRepository(InMemoryRepository[Database, str]):
    pass