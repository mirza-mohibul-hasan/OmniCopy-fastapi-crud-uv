## Running the Application

You can start the FastAPI application using either of the following commands:

```bash
# Using uv's FastAPI integration
uv run fastapi dev .\main.py

# Or using Uvicorn directly with auto-reload enabled
uv run uvicorn main:app --reload
```

Choose the method that best fits your workflow.

""" Data Structures
Campaigns
- campaign_id: int
- name: str
- due_date: str
- created_at: str

pieces
- piece_id: int
- campaign_id: int
- name: str
- content: str
- content_type: str
- created_at: str
"""