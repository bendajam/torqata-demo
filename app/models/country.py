from app.database import db
from .base import BaseModel


class Country(BaseModel):
    """Country show is provided in."""
    name = db.Column(db.String)
