from fastapi import Depends
from sqlalchemy.orm import Session
from . import models
from .database import get_db
import hashlib
import secrets


def create_api_key(admin_id: models.Admins, db: Session):
    key = secrets.token_urlsafe(40)

    key_hash = hashlib.sha256(key.encode()).hexdigest()

    db_key = models.APIKey(admin_id=admin_id, key_hash=key_hash)
    db.add(db_key)
    db.commit()
    db.refresh(db_key)
    return {"api_key": key, "created_at": db_key.created_at}


def get_current_admin():
    pass
