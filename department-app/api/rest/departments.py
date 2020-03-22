"""Contains resources for performing CRUD operations on department table.

Exported classes:
    DepartmentsApi: a resource, containing GET and POST request handlers.
    DepartmentApi: a resource, containing GET, PUT and DELETE request handlers.
"""

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from flask_restful import Resource, reqparse

from models.department import Department
from service.operator import Operator
from rest.utility.jsonresponse import data_response, error_response

PARSER = reqparse.RequestParser()


# pylint: disable=R0201
class DepartmentsApi(Resource):
    """Contains GET and POST request handlers for department table.

    Given class groups handlers which do not require item's id to
    perform a database request.
    """

    def get(self):
        """Returns all the departments from the db using data_response."""

        departments = Operator.get_all(Department)
        return data_response(Department.json_list(departments))

    def post(self):
        """Adds a department to the database.

        Returns:
            Department's id using data_response or
            error object using error_response.
        """

        PARSER.add_argument('name', type=str)
        try:
            raw_data = PARSER.parse_args()
            department = Department(name=raw_data['name'])
            Operator.insert(department)
            return data_response(department.id)
        except IntegrityError:
            return error_response(404)


class DepartmentApi(Resource):
    """Contains GET (by id), PUT and DELETE request handlers for department table.

    Given class groups handlers which require item's id to
    perform a database request.
    """

    def get(self, id_):
        """Gets a department from the database by the id.

        Returns:
            Retreived department using data_response or
            error object using error_response.
        """

        try:
            department = Operator.get_by_id(Department, id_)
            return data_response(department.json())
        except AttributeError:
            return error_response(404)

    def put(self, id_):
        """Updates a department from the database by the id.

        Returns:
            True (if the operation was successful)
            or False using data_response or
            error object using error_response.
        """

        PARSER.add_argument('name', type=str)
        try:
            raw_data = PARSER.parse_args()
            raw_data['id'] = id_
            return data_response(Operator.update(Department, raw_data))
        except IntegrityError:
            return error_response(400)

    def delete(self, id_):
        """Deletes a department from the database by the id.

        Returns:
            All the departments from the db using data_response or
            error object using error_response.
        """

        try:
            Operator.remove(Department, id_)
            return data_response(Department.json_list(Operator.get_all(Department)))
        except UnmappedInstanceError:
            return error_response(404)
