from flask_restful import fields


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
