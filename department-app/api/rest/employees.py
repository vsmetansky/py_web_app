"""Contains resources for performing CRUD operations on employee table.

Exported classes:
    EmployeesApi: a resource, containing GET and POST request handlers.
    EmployeeApi: a resource, containing GET, PUT and DELETE request handlers.
"""

from sqlalchemy.exc import IntegrityError, InternalError, ArgumentError
from marshmallow import fields, ValidationError
from flask_restful import Resource, abort
from flask import request

from models.employee import Employee
from service.operator import Operator
from rest.schemas.employee import EmployeeSchema, EmployeeSearchSchema
from rest.schemas.funcs import lomarsh, marsh_with, marsh_with_field


# pylint: disable=R0201
class EmployeesApi(Resource):
    """Contains GET and POST request handlers for employee table.

    Groups handlers which do not require item's id to
    perform a database request.
    """

    @marsh_with(EmployeeSchema, to_many=True)
    def get(self):
        """Returns filtered list of employees from the db using marshal."""
        try:
            search_params = lomarsh(request.args, EmployeeSearchSchema)
            return Operator.get_all(Employee, search_expr=self._get_search_expr(search_params))
        except ValidationError:
            abort(400)

    @marsh_with_field(fields.Integer())
    def post(self):
        """Adds an employee to the database.

        Returns:
            Employee's id using marshal or
            aborts with code 400.
        """

        try:
            raw_data = lomarsh(request.form, EmployeeSchema)
            raw_data['id'] = None
            return Operator.insert(Employee(**raw_data))
        except (IntegrityError, ValidationError):
            abort(400)

    # pylint: disable=E1101
    def _get_search_expr(self, s_params):
        try:
            search_expr = [
                Employee.birthdate >= s_params.get('begin'),
                Employee.birthdate <= s_params.get('end')
            ]
            if s_params.get('name'):
                search_expr.append(Employee.name.like(
                    f'%{s_params.get("name")}%'))
            return search_expr
        except ArgumentError:
            return None


class EmployeeApi(Resource):
    """Contains GET (by id), PUT and DELETE request handlers for employee table.

    Given class groups handlers which require item's id to
    perform a database request.
    """

    @marsh_with(EmployeeSchema)
    def get(self, id_):
        """Gets an employee from the database by the id.

        Returns:
            Retreived employee using marshal or
            aborts with 404 code.
        """

        entity = Operator.get_by_id(Employee, id_)
        return entity if entity else abort(404)

    @marsh_with_field(fields.Boolean())
    def put(self, id_):
        """Updates an employee from the database by the id.

        Returns:
            True (if the operation was successful)
            or False using marshal or aborts
            with 400 code.
        """

        try:
            raw_data = lomarsh(request.form, EmployeeSchema)
            raw_data['id'] = id_
            return Operator.update(Employee, raw_data)
        except (IntegrityError, InternalError, ValidationError):
            abort(400)

    # pylint: disable=R1710
    @marsh_with(EmployeeSchema, to_many=True)
    def delete(self, id_):
        """Deletes an employee from the database by the id.

        Returns:
            All the employees from the db using marshal or
            aborts with 404 code.
        """

        if Operator.remove(Employee, id_):
            return Operator.get_all(Employee)
        abort(404)
