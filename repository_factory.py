from repositories.inmemory.in_memory_database_repository import InMemoryDatabaseRepository

class RepositoryFactory:
    @staticmethod
    def get_database_repository(storage_type: str):
        if storage_type == "MEMORY":
            return InMemoryDatabaseRepository()
        elif storage_type == "DATABASE":
            raise NotImplementedError("Database storage not implemented yet.")
        else:
            raise ValueError(f"Invalid storage type: {storage_type}")