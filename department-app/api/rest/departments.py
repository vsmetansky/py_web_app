"""Contains resources for performing CRUD operations on department table.

Exported classes:
    DepartmentsApi: a resource, containing GET and POST request handlers.
    DepartmentApi: a resource, containing GET, PUT and DELETE request handlers.
"""

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from flask_restful import (
    Resource, reqparse, marshal_with,
    marshal_with_field, abort, fields
)

from models.department import Department
from service.operator import Operator
from rest.utility.fields import DEPARTMENT_FIELDS

PARSER = reqparse.RequestParser()


# pylint: disable=R0201
class DepartmentsApi(Resource):
    """Contains GET and POST request handlers for department table.

    Given class groups handlers which do not require item's id to
    perform a database request.
    """

    @marshal_with(DEPARTMENT_FIELDS)
    def get(self):
        """Returns all the departments from the db using marshal."""
        return Operator.get_all(Department)

    @marshal_with_field(fields.Integer)
    def post(self):
        """Adds a department to the database.

        Returns:
            Department's id using marshal or
            aborts with 404.
        """

        PARSER.add_argument('name', type=str)
        try:
            raw_data = PARSER.parse_args()
            department = Department(name=raw_data['name'])
            return Operator.insert(department)
        except IntegrityError:
            abort(400)


class DepartmentApi(Resource):
    """Contains GET (by id), PUT and DELETE request handlers for department table.

    Given class groups handlers which require item's id to
    perform a database request.
    """

    @marshal_with(DEPARTMENT_FIELDS)
    def get(self, id_):
        """Gets a department from the database by the id.

        Returns:
            Retreived department using marshal or
            aborts with 404 if department was not present.
        """

        entity = Operator.get_by_id(Department, id_)
        return entity if entity else abort(404)

    @marshal_with_field(fields.Boolean)
    def put(self, id_):
        """Updates a department from the database by the id.

        Returns:
            True (if the operation was successful)
            or False using marshal or aborts with
            code 400.
        """

        PARSER.add_argument('name', type=str)
        try:
            raw_data = PARSER.parse_args()
            raw_data['id'] = id_
            return Operator.update(Department, raw_data)
        except IntegrityError:
            abort(400)

    @marshal_with(DEPARTMENT_FIELDS)
    def delete(self, id_):
        """Deletes a department from the database by the id.

        Returns:
            All the departments from the db using marshal or
            aborts with 404 code.
        """

        if Operator.remove(Department, id_):
            return Operator.get_all(Department)
        abort(404)
