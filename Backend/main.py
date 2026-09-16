from fastapi import FastAPI

from Backend.routers.accounts import router as accounts_router


app = FastAPI(
    title="My Layered Backend API",
    description="Testing business logic with hardcoded data",
)

app.include_router(accounts_router)


@app.get("/")
def read_root():
    return {"message": "Citi Bank API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


