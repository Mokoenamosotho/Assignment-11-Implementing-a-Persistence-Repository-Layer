import json
from typing import Optional
from repositories.inmemory.in_memory_database_repository import Database

class FileSystemDatabaseRepository:
    def __init__(self, file_path: str):
        self._file_path = file_path

    def save(self, database: Database) -> None:
        databases = self._load_all()
        databases[database.id] = {
            "id": database.id,
            "name": database.name
        }
        with open(self._file_path, 'w') as f:
            json.dump(databases, f)

    def find_by_id(self, id: str) -> Optional[Database]:
        databases = self._load_all()
        data = databases.get(id)
        if data:
            return Database(id=data['id'], name=data['name'])
        return None

    def _load_all(self) -> dict:
        try:
            with open(self._file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}