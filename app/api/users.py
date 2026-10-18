from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database import crud

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def create_user(
    name: str,
    email: str,
    db: Session = Depends(get_db)
):
    user = crud.create_user(
        db=db,
        name=name,
        email=email
    )

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }


@router.get("/")
def get_users(
    db: Session = Depends(get_db)
):
    users = crud.get_users(db)

    return [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
        for user in users
    ]