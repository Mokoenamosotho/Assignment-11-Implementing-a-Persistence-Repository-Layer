from typing import TypeVar, Generic, Optional, Dict

T = TypeVar('T')
ID = TypeVar('ID')

class InMemoryRepository(Generic[T, ID]):
    def __init__(self):
        self._storage: Dict[ID, T] = {}

    def save(self, entity: T, entity_id: ID) -> None:
        self._storage[entity_id] = entity

    def find_by_id(self, entity_id: ID) -> Optional[T]:
        return self._storage.get(entity_id)

    def delete_by_id(self, entity_id: ID) -> None:
        if entity_id in self._storage:
            del self._storage[entity_id]

    def find_all(self) -> Dict[ID, T]:
        return self._storage.copy()