"""Declares schemas for 'employees' route.

Exported classes:
    EmployeeSchema: Schema mapping for 'Employee' model.
    EmployeeSearchSchema: Schema for performing searches on 'Employee' resources.
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


class EmployeeSearchSchema(Schema):
    """Schema for performing searches on 'Employee' resources."""

    name = fields.Str()
    begin = fields.Str()
    end = fields.Str()

    @validates_schema
    def validate_birth_range(self, data, **kwargs):
        try:
            if data.get('begin'):
                datetime.strptime(data.get('begin'), '%Y-%m-%d').date()
            if data.get('end'):
                datetime.strptime(data.get('end'), '%Y-%m-%d').date()
        except ValueError as e:
            raise ValidationError(e)
