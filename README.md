# Repository and Storage Abstraction

## In-Memory Repository

Implemented a generic in-memory repository using Python's Dictionary (HashMap).
- Promotes reusability via `InMemoryRepository<T, ID>`.
- Specialized example: `InMemoryDatabaseRepository` for managing `Database` entities.

## Storage Abstraction: Factory Pattern

**Pattern Chosen:** Factory Pattern

### Why Factory Pattern?
- **Flexibility**: Swap between storage backends easily.
- **Future-Proofing**: Add new implementations (e.g., real databases) without changing service code.
- **Consistency**: Central point of repository instantiation.

### How It Works
- `RepositoryFactory.get_database_repository("MEMORY")` → returns an in-memory implementation.
- Support for future `"DATABASE"` backend is already planned.

---

**Testing**
- Verified CRUD operations for `InMemoryDatabaseRepository`.
- Verified factory returns correct instances and raises appropriate errors.