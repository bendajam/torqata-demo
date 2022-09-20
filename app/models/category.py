from .base import BaseModel
from app import db

"""
"""
class Category(BaseModel):
  title = db.Column(db.String)