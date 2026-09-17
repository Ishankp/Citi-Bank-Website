# Citi Bank Website

## Run the Backend

From the project root, create the virtual environment once:

```powershell
python -m venv .venv
```

Install the backend dependencies:

```powershell
& ".venv\Scripts\python.exe" -m pip install -r requirements
```

Copy `.env.example` to `.env` and fill in your real Supabase database password (percent-encode
any special characters, e.g. `@` -> `%40`). `Backend/database.py` reads `DATABASE_URL` from this
file to connect to the Supabase Postgres instance.

Start the FastAPI development server:

```powershell
& ".venv\Scripts\python.exe" -m uvicorn Backend.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

Interactive API documentation is available at:

`http://127.0.0.1:8000/docs`

The current version uses hardcoded account data.

## Backend Structure

```text
Backend/
├── main.py             # Creates the FastAPI app and registers routers
├── routers/            # HTTP endpoints and request/response handling
├── services/           # Business logic
├── repositories/       # Data access operations
├── data/               # Temporary hardcoded data
└── schemas/            # Pydantic API models and validation
```

The request flow is:

```text
Router -> Service -> Repository -> Data
```
