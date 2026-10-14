from fastapi import APIRouter, status, HTTPException, responses, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils, oauth2

router = APIRouter(prefix=("/message"), tags=["Message"])


@router.post("/")
def message(email: schemas.Email, db: Session = Depends(get_db)):

    new_message = models.Emails(
        admin_id=oauth2.verify_token,
        sender_email=email.sender_email,
        subject=email.subject,
    )
    db.add(new_message)
    db.commit()
    db.refresh()
    return "Email Sent Sucessfully!!"
