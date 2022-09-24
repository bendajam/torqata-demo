from app import db
from .base import BaseModel


class Category(BaseModel):
    """Category of show."""
    title = db.Column(db.String)
