from repositories.inmemory.in_memory_database_repository import InMemoryDatabaseRepository
from repositories.filesystem.file_system_database_repository import FileSystemDatabaseRepository

class RepositoryFactory:
    @staticmethod
    def get_database_repository(storage_type: str, file_path: str = "database_storage.json"):
        if storage_type == "MEMORY":
            return InMemoryDatabaseRepository()
        elif storage_type == "FILESYSTEM":
            return FileSystemDatabaseRepository(file_path)
        elif storage_type == "DATABASE":
            raise NotImplementedError("Database storage not implemented yet.")
        else:
            raise ValueError(f"Invalid storage type: {storage_type}")