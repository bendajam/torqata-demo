from app.database import db
from .base import BaseModel


class Person(BaseModel):
    name = db.Column(db.String)
