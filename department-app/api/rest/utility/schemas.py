""" Provides routes with marshal serialization dictionaries.

Exported objects:
    EMPLOYEE_FIELDS: A dictionary of marhal fields for Employee model.
    DEPARTMENT_FIELDS: A dictionary of marhal fields for Department model.
"""

from ma import fields

EMPLOYEE_FIELDS = {
    'id': fields.Integer,
    'department_id': fields.Integer,
    'name': fields.String,
    'salary': fields.Integer,
    'birthdate': fields.String
}

DEPARTMENT_FIELDS = {
    'id': fields.Integer,
    'name': fields.String,
    'employees': fields.List(fields.Nested(EMPLOYEE_FIELDS))
}
