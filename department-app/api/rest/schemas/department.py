"""Declares schemas for 'departments' route."""

from marshmallow import Schema, fields

from models.department import Department


class DepartmentSchema(Schema):
    """Schema mapping for 'Department' model."""

    id = fields.Integer()
    name = fields.Str()


class DepartmentSearchSchema():
    pass
