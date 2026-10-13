import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from .config import settings
from . import schemas

oauth2_schema = OAuth2PasswordBearer("login")

SECRECT_KEY = settings.secrect_key

ALGORITHM = settings.algorithm

ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encode_jwt = jwt.encode(to_encode, SECRECT_KEY, algorithm=ALGORITHM)
    return encode_jwt


def verify_token(token: str, details_exception):
    try:
        payload = jwt.decode(token, SECRECT_KEY, algorithm=ALGORITHM)

        id: int = payload.get("admin_id")
        if id is None:
            raise details_exception
        token = schemas.TokenData(admin_id=id)
    except InvalidTokenError:
        raise details_exception
    return token.admin_id


def get_current_admin(token: str):
    details_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Couldn't validate details.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, details_exception)
