# Alembic Migration Usage Guide

## Common Commands

All commands should be run inside the Docker container:

```bash
docker compose exec backend uv run alembic <command>
```

### Check Current Version
```bash
docker compose exec backend uv run alembic current
```

### View Migration History
```bash
docker compose exec backend uv run alembic history --verbose
```

### Create a New Migration

After modifying models in `app/models/`:

```bash
docker compose exec backend uv run alembic revision --autogenerate -m "Description of changes"
```

### Apply Migrations

Upgrade to latest version:
```bash
docker compose exec backend uv run alembic upgrade head
```

Upgrade one version:
```bash
docker compose exec backend uv run alembic upgrade +1
```

### Rollback Migrations

Downgrade one version:
```bash
docker compose exec backend uv run alembic downgrade -1
```

Downgrade to base:
```bash
docker compose exec backend uv run alembic downgrade base
```

### Show SQL Without Applying

View SQL that would be executed:
```bash
docker compose exec backend uv run alembic upgrade head --sql
```

## Workflow Example

1. Modify a model (e.g., add a field to `User`)
2. Generate migration:
   ```bash
   docker compose exec backend uv run alembic revision --autogenerate -m "Add user phone field"
   ```
3. Review generated migration file in `alembic/versions/`
4. Apply migration:
   ```bash
   docker compose exec backend uv run alembic upgrade head
   ```
5. If issues occur, rollback:
   ```bash
   docker compose exec backend uv run alembic downgrade -1
   ```

## Important Notes

- Always review auto-generated migrations before applying
- Alembic may not detect all changes (like renamed columns)
- For complex schema changes, edit migration files manually
- Never modify applied migrations - create new ones instead
- Keep migrations in version control
