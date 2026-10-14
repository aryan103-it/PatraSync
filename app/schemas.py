from pydantic import BaseModel, EmailStr


class AdminCreate(BaseModel):
    email: EmailStr
    password: str
    receiver_email: EmailStr


class AdminResponse(BaseModel):
    id: int
    email: EmailStr
    receiver_email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    admin_id: int


class Email(BaseModel):
    sender_email: str
    subject: str
    body: str
