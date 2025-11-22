# Task Manager API
Simple task management system built with Django and DRF.

## Requirements
- Docker and Docker Compose.
- (Optional) Python 3.13 and Poetry for local development.

## Running with Docker
```bash
make up
```
API will be available at http://localhost:8000/api/.

## JWT endpoints
- `POST /api/token/` — obtain access/refresh.
- `POST /api/token/refresh/` — refresh access token.

## Docs
- Swagger UI: http://localhost:8000/api/schema/swagger/
- Redoc: http://localhost:8000/api/schema/redoc/

## Running tests
```bash
make test
```

## Formatting
```bash
make format
```
