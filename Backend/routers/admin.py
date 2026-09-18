from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Backend.database import get_db
from Backend.dependencies import require_admin
from Backend.schemas.account import Users
from Backend.services.user_service import list_all_customers

router = APIRouter(prefix="/api/admin", tags=["Admin"])


@router.get("/users", response_model=list[Users])
def list_users(db: Session = Depends(get_db), _admin=Depends(require_admin)):
    return list_all_customers(db)
