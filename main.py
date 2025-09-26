"""
Legacy entry point - imports the restructured app
For development, use: uv run fastapi dev app/main.py
"""
from app.main import app

__all__ = ["app"]