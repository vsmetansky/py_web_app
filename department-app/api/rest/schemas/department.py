"""Declares schemas for 'departments' route."""

from marshmallow import Schema, fields

from models.department import Department
from rest.schemas.employee import EmployeeSchema


class DepartmentSchema(Schema):
    """Schema mapping for 'Department' model."""

    id = fields.Integer()
    name = fields.Str()
    employees = fields.List(fields.Nested(EmployeeSchema))


class DepartmentSearchSchema(Schema):
    """Schema for performing searches on 'Department' resources."""

    name = fields.Str()
