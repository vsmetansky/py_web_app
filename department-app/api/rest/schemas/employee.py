"""Declares schemas for 'employees' route."""


from marshmallow import Schema, fields

from models.employee import Employee


class EmployeeSchema(Schema):
    """Schema mapping for 'Employee' model."""

    id = fields.Integer()
    name = fields.Str()
    department_id = fields.Integer()
    salary = fields.Integer()
    birthdate = fields.Str()
