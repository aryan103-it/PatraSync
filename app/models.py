from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from .database import Base


class Admins(Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    receiver_email = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))


class Emails(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True, nullable=False)
    admin_id = Column(
        Integer, ForeignKey("admins.id", ondelete="CASCADE"), nullable=False
    )
    sender_email = Column(String, nullable=False)
    subject = Column(String)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))

    admin = relationship("Admins")


class APIKey(Base):
    __tablename__ = "api_key"
    id = Column(Integer, primary_key=True, nullable=False)
    admin_id = Column(
        Integer, ForeignKey("admins.id", ondelete="CASCADE"), nullable=False
    )
    key_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))

    admin = relationship("Admins")
