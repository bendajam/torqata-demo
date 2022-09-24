from marshmallow_sqlalchemy import fields
from app import ma, models


class CategorySchema(ma.SQLAlchemySchema):
    """Category marshmellow schema."""
    class Meta:
        """Link sqlalchemy model."""
        model = models.Category

    id = ma.auto_field()
    title = ma.auto_field()


class CountrySchema(ma.SQLAlchemySchema):
    """Country marshmellow schema."""
    class Meta:
        """Link sqlalchemy model."""
        model = models.Country

    id = ma.auto_field()
    name = ma.auto_field()

    # model schema for marshmallow


class ShowSchema(ma.SQLAlchemyAutoSchema):
    """Show marshmellow schema."""
    class Meta:
        """Link sqlalchemy model."""
        model = models.Show


class PersonSchema(ma.SQLAlchemySchema):
    """Person marshmellow schema."""
    class Meta:
        """Link sqlalchemy model."""
        model = models.Person

    id = ma.auto_field()
    name = ma.auto_field()


class PersonDetailSchema(ma.SQLAlchemySchema):
    """Person Details marshmellow schema."""
    class Meta:
        """Link sqlalchemy model."""
        model = models.Person

    id = ma.auto_field()
    name = ma.auto_field()

    cast = fields.Nested(ShowSchema, many=True)
    directed = fields.Nested(ShowSchema, many=True)

# model schema for marshmallow


class ShowDetailSchema(ma.SQLAlchemyAutoSchema):
    """Show Details marshmellow schema."""
    class Meta:
        """Link sqlalchemy model."""
        model = models.Show

    directors = fields.Nested(PersonSchema, many=True)
    cast = fields.Nested(PersonSchema, many=True)
    countries = fields.Nested(CountrySchema, many=True)
    categories = fields.Nested(CategorySchema, many=True)
