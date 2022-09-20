from .base import BaseModel, BaseJoinModel
from app import db

"""
"""
class Show(BaseModel):
  show_id = db.Column(db.String)
  title = db.Column(db.String)

  show_type = db.Column(db.String)
  description = db.Column(db.String)
  rating = db.Column(db.String)

  date_added = db.Column(db.Date)
  release_year = db.Column(db.Integer)

  duration = db.Column(db.Integer)

  cast = db.relationship("Person", secondary="show_cast", backref="cast")
  directors = db.relationship("Person", secondary="show_director", backref="directed" )
  countries = db.relationship("Country", secondary="show_country", backref="shows")
  categories = db.relationship("Category", secondary="show_category", backref="shows")

  def to_dict(self):
    return {
      "id": self.id,
      "title": self.title,
      "description": self.description
    }

class ShowDirector(BaseJoinModel):
  __tablename__ = "show_director"

  show_id = db.Column(db.ForeignKey("show.id"), primary_key=True)
  person_id = db.Column(db.ForeignKey("person.id"), primary_key=True)

class ShowCast(BaseJoinModel):
  __tablename__ = "show_cast"

  show_id = db.Column(db.ForeignKey("show.id"), primary_key=True)
  person_id = db.Column(db.ForeignKey("person.id"), primary_key=True)

class ShowCountry(BaseJoinModel):
  __tablename__ = "show_country"

  show_id = db.Column(db.ForeignKey("show.id"), primary_key=True)
  country_id = db.Column(db.ForeignKey("country.id"), primary_key=True)

class ShowCategory(BaseJoinModel):
  __tablename__ = "show_category"

  show_id = db.Column(db.ForeignKey("show.id"), primary_key=True)
  category_id = db.Column(db.ForeignKey("category.id"), primary_key=True)
