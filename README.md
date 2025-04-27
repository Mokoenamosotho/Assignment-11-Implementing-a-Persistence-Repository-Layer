# Repositories Design Justification

## Why use a generic Repository interface?

We implemented a generic `Repository<T, ID>` interface to promote reusability and avoid code duplication across different entity repositories.

- **DRY Principle**: "Don't Repeat Yourself" – no need to redefine standard CRUD operations for every entity.
- **Flexibility**: New entities can easily create their own repositories by simply extending the generic interface.
- **Maintainability**: If CRUD signatures need to change, they can be updated in one place only.
- **Scalability**: The system can scale to many entities without growing boilerplate code.

Each entity-specific repository (e.g., `DatabaseRepository`, `BackupRepository`, etc.) extends `Repository<T, ID>`, where `T` is the entity class and `ID` is the type of the entity’s primary key (usually `String` for UUIDs).
