from app import ma, models
from marshmallow_sqlalchemy import fields 

class CategorySchema(ma.SQLAlchemySchema):
  class Meta:
    model = models.Category 
  
  id = ma.auto_field()
  title = ma.auto_field()

class CountrySchema(ma.SQLAlchemySchema):
  class Meta:
    model = models.Country 

  id = ma.auto_field()
  name = ma.auto_field()

  # model schema for marshmallow
class ShowSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = models.Show

class PersonSchema(ma.SQLAlchemySchema):
  class Meta:
    model = models.Person

  id = ma.auto_field()
  name = ma.auto_field()

class PersonDetailSchema(ma.SQLAlchemySchema):
  class Meta:
    model = models.Person

  id = ma.auto_field()
  name = ma.auto_field()

  cast = fields.Nested(ShowSchema, many=True)
  directed = fields.Nested(ShowSchema, many=True)

# model schema for marshmallow
class ShowDetailSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = models.Show

  directors = fields.Nested(PersonSchema, many=True)
  cast = fields.Nested(PersonSchema, many=True)
  countries = fields.Nested(CountrySchema, many=True)
  categories = fields.Nested(CategorySchema, many=True)
