from .base import BaseModel
from app import db

class Country(BaseModel):
  name = db.Column(db.String)