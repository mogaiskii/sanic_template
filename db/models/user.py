from sqlalchemy import Column, VARCHAR

from .base import DBModel


class User(DBModel):
    __tablename__ = 'users'

    login = Column(VARCHAR(128), nullable=False, index=True, unique=True)
    password_hash = Column(VARCHAR(256), nullable=False, index=True)
