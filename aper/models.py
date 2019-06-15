from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import func
from .db import Base, db_session


class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer,
                primary_key=True)  # primary keys are required by SQLAlchemy
    email = Column(String(100), unique=True)
    name = Column(String(100))
    order = Column(Integer, nullable=False)

    def __init__(self, name, email):
        self.email = email
        self.name = name
        max_order = db_session.query(func.max(User.order)).scalar()
        self.order = max_order + 1 if max_order else 1

    def __repr__(self):
        return '<User {}[{}]>'.format(self.name, self.email)

    def serialize(self):
        """Return object data in serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'order': self.order
        }
