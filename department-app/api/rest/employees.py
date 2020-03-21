"""Contains resources for performing CRUD operations on employee table.

Exported classes:
    EmployeesApi: a resource, containing GET and POST request handlers.
    EmployeeApi: a resource, containing GET, PUT and DELETE request handlers.
"""

from datetime import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from flask_restful import Resource, reqparse

from models.employee import Employee
from service.operator import Operator
from rest.utility.jsonresponse import data_response, error_response

PARSER = reqparse.RequestParser()


def add_employee_args():
    """Adds arguments to the parser"""

    PARSER.add_argument('name', type=str)
    PARSER.add_argument('salary', type=int)
    PARSER.add_argument('birthdate', type=str)
    PARSER.add_argument('department_id', type=int)


# pylint: disable=R0201
class EmployeesApi(Resource):
    """Contains GET and POST request handlers for employee table.

    Given class groups handlers which do not require item's id to
    perform a database request.
    """

    def get(self):
        """Returns all the employees from the db using data_response."""

        employees = Operator.get_all(Employee)
        return data_response(Employee.json_list(employees))

    def post(self):
        """Adds an employee to the database.

        Returns:
            Employee's id using data_response or
            error object using error_response.
        """

        add_employee_args()
        try:
            raw_data = PARSER.parse_args()
            employee = self.__employee_from_raw(raw_data)
            Operator.insert(employee)
            return data_response(employee.id)
        except IntegrityError:
            return error_response(400)

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

    def get(self, id_):
        """Gets an employee from the database by the id.

        Returns:
            Retreived employee using data_response or
            error object using error_response.
        """

        try:
            employee = Operator.get_by_id(Employee, id_)
            return data_response(employee.json())
        except AttributeError:
            return error_response(404)

    def put(self, id_):
        """Updates an employee from the database by the id.

        Returns:
            True (if the operation was successful)
            or False using data_response or
            error object using error_response.
        """

        add_employee_args()
        try:
            raw_data = PARSER.parse_args()
            raw_data['id'] = id_
            return data_response(Operator.update(Employee, raw_data))
        except IntegrityError:
            return error_response(404)

    def delete(self, id_):
        """Deletes an employee from the database by the id.

        Returns:
            All the employees from the db using data_response or
            error object using error_response.
        """

        try:
            Operator.remove(Employee, id_)
            return data_response(Employee.json_list(Operator.get_all(Employee)))
        except UnmappedInstanceError:
            return error_response(404)
