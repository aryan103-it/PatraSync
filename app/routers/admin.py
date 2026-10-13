from fastapi import APIRouter, status, HTTPException, responses, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils

router = APIRouter(prefix="/admins", tags=["Admins"])


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.AdminResponse
)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):

    hashed_password = utils.hash(admin.password)
    admin.password = hashed_password
    new_admin = models.Admins(**admin.dict())
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin
