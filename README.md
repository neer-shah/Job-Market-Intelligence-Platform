# Job-Market-Intelligence-Platform
A Job Market Intelligence Platform collects job postings from one or more sources, stores them in a database, processes the text, and exposes insights through an API or dashboard.


# Running venv
python -m venv .venv
.\.venv\Scripts\activate.ps1

# Core packages
pip install fastapi uvicorn httpx sqlalchemy psycopg[binary] python-dotenv pydantic