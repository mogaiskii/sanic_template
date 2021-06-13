from sqlalchemy import Column, VARCHAR

from .base import DBModel


class User(DBModel):
    __tablename__ = 'users'

    login = Column(VARCHAR(128), nullable=False)
