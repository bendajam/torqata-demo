from .base import BaseModel
from app import db

class Person(BaseModel):
  name = db.Column(db.String)
