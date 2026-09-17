from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Backend import models
from Backend.database import Base, engine
from Backend.routers.accounts import router as accounts_router
from Backend.routers.users import router as users_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My Layered Backend API",
    description="Testing business logic with hardcoded data",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(accounts_router)
app.include_router(users_router)


@app.get("/")
def read_root():
    return {"message": "Citi Bank API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


