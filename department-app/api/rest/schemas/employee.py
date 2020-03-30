"""Declares schemas for 'employees' route.

Exported classes:
    EmployeeSchema: blah.
"""

from datetime import datetime

from marshmallow import Schema, fields, validates_schema, ValidationError

from models.employee import Employee


class EmployeeSchema(Schema):
    """Schema mapping for 'Employee' model."""

    id = fields.Integer()
    name = fields.Str()
    department_id = fields.Integer()
    salary = fields.Integer()
    birthdate = fields.Str()

    @validates_schema
    def validate_birthdate(self, data, **kwargs):
        try:
            datetime.strptime(data['birthdate'], '%Y-%m-%d').date()
        except ValueError as e:
            raise ValidationError(e)
