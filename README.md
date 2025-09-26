# OmniCopy FastAPI CRUD Application

A FastAPI application for managing marketing campaigns with SQLite database using SQLModel.

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── main.py              # Main FastAPI application
│   ├── api/
│   │   ├── __init__.py
│   │   └── campaigns.py     # Campaign API routes
│   ├── core/
│   │   ├── __init__.py
│   │   └── database.py      # Database configuration
│   ├── models/
│   │   ├── __init__.py
│   │   └── campaign.py      # SQLModel database models
│   └── schemas/
│       ├── __init__.py
│       └── campaign.py      # Pydantic schemas for request/response
├── database.db             # SQLite database file
├── main.py                 # Legacy entry point (imports app.main)
├── pyproject.toml          # Project dependencies
└── README.md
```

## Features

- **FastAPI** with automatic API documentation
- **SQLModel** for database operations with type safety
- **SQLite** database with automatic table creation
- **Pydantic** schemas for request/response validation
- **CRUD operations** for campaigns
- **Generic response models** for consistent API responses
- **Proper error handling** with HTTP status codes

## API Endpoints

### Campaigns

- `GET /api/v1/` - Health check
- `GET /api/v1/campaigns/` - Get all campaigns
- `GET /api/v1/campaigns/{id}` - Get campaign by ID
- `POST /api/v1/campaigns/` - Create new campaign
- `PUT /api/v1/campaigns/{id}` - Update campaign
- `DELETE /api/v1/campaigns/{id}` - Delete campaign

## Running the Application

You can start the FastAPI application using either of the following commands:

### Development Server (Recommended)
```bash
# Using the new structured app
uv run fastapi dev app/main.py

# Or using the legacy entry point
uv run fastapi dev main.py
```

### Production Server
```bash
# Using Uvicorn directly
uv run uvicorn app.main:app --reload

# Or using the legacy entry point
uv run uvicorn main:app --reload
```

The API will be available at:
- API: http://localhost:8000/api/v1/
- Interactive docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Database Schema

### Campaign Model
```python
{
    "campaign_id": int,      # Primary key (auto-generated)
    "name": str,             # Campaign name
    "due_date": datetime,    # Campaign due date (optional)
    "created_at": datetime   # Auto-generated timestamp
}
```

## Sample Data

The application automatically creates sample campaigns on first startup:
- Summer Launch
- Black Friday
- Holiday Sale
- Spring Promo
- Back to School
- Winter Clearance

## Development

The project uses:
- **uv** for dependency management
- **SQLModel** for database operations
- **FastAPI** for the web framework
- **SQLite** for the database

Choose the development method that best fits your workflow.