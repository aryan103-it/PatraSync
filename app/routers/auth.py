from fastapi import APIRouter, status, HTTPException, responses, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils, oauth2, api_key

router = APIRouter(prefix="/login", tags=["Login"])


@router.post("/", response_model=schemas.Token)
def login(
    admin_details: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    admin = (
        db.query(models.Admins)
        .filter(models.Admins.email == admin_details.username)
        .first()
    )
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid email or password."
        )

    if not utils.verify_password(admin_details.password, admin.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid email or password."
        )

    access_token = oauth2.create_token(data={"admin_id": admin.id})

    return {"access_token": access_token, "token_type": "Bearer"}


@router.get("/generate")
def generate_api_key(
    current_admin: models.Admins = Depends(oauth2.get_current_admin),
    db: Session = Depends(get_db),
):
    return api_key.create_api_key(current_admin, db)
