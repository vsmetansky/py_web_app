"""Contains resources for performing CRUD operations on employee table.

Exported classes:
    EmployeesApi: a resource, containing GET and POST request handlers.
    EmployeeApi: a resource, containing GET, PUT and DELETE request handlers.
"""

from datetime import datetime

from sqlalchemy.exc import IntegrityError, InternalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from flask_restful import (
    Resource, reqparse, marshal_with,
    marshal_with_field, abort, fields
)

from models.employee import Employee
from service.operator import Operator
from rest.utility.fields import EMPLOYEE_FIELDS


PARSER = reqparse.RequestParser()


def add_employee_args():
    """Adds arguments to the parser"""
    PARSER.add_argument('name', type=str)
    PARSER.add_argument('salary', type=int)
    PARSER.add_argument('birthdate', type=str)
    PARSER.add_argument('department_id', type=int)


def add_search_query_args():
    """Adds search arguments to the parser"""
    PARSER.add_argument('name', type=str, location='args')
    PARSER.add_argument('salary', type=int, location='args')
    PARSER.add_argument('birthdate', type=str, location='args')


# pylint: disable=R0201
class EmployeesApi(Resource):
    """Contains GET and POST request handlers for employee table.

    Groups handlers which do not require item's id to
    perform a database request.
    """

    @marshal_with(EMPLOYEE_FIELDS)
    def get(self):
        """Returns filtered list of employees from the db using marshal."""
        return Operator.get_all(Employee)

    @marshal_with_field(fields.Integer)
    def post(self):
        """Adds an employee to the database.

        Returns:
            Employee's id using marshal or
            aborts with code 400.
        """

        add_employee_args()
        try:
            raw_data = PARSER.parse_args()
            employee = self.__employee_from_raw(raw_data)
            return Operator.insert(employee)
        except (IntegrityError, ValueError) as e:
            abort(400)

    def __employee_from_raw(self, raw_data):
        return Employee(department_id=raw_data['department_id'],
                        name=raw_data['name'], salary=raw_data['salary'],
                        birthdate=self.__date_from_raw(raw_data['birthdate']))

    def __date_from_raw(self, raw_date):
        return datetime.strptime(raw_date, '%Y-%m-%d').date()


class EmployeeApi(Resource):
    """Contains GET (by id), PUT and DELETE request handlers for employee table.

    Given class groups handlers which require item's id to
    perform a database request.
    """

    @marshal_with(EMPLOYEE_FIELDS)
    def get(self, id_):
        """Gets an employee from the database by the id.

        Returns:
            Retreived employee using marshal or
            aborts with 404 code.
        """

        entity = Operator.get_by_id(Employee, id_)
        return entity if entity else abort(404)

    @marshal_with_field(fields.Boolean)
    def put(self, id_):
        """Updates an employee from the database by the id.

        Returns:
            True (if the operation was successful)
            or False using marshal or aborts
            with 400 code.
        """

        add_employee_args()
        try:
            raw_data = PARSER.parse_args()
            raw_data['id'] = id_
            return Operator.update(Employee, raw_data)
        except (IntegrityError, InternalError) as e:
            abort(400)

    @marshal_with(EMPLOYEE_FIELDS)
    def delete(self, id_):
        """Deletes an employee from the database by the id.

        Returns:
            All the employees from the db using marshal or
            aborts with 404 code.
        """

        if Operator.remove(Employee, id_):
            return Operator.get_all(Employee)
        abort(404)
