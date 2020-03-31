"""Contains resources for performing CRUD operations on department table.

Exported classes:
    DepartmentsApi: a resource, containing GET and POST request handlers.
    DepartmentApi: a resource, containing GET, PUT and DELETE request handlers.
"""

from sqlalchemy.exc import IntegrityError
from flask_restful import Resource, abort
from marshmallow import fields, ValidationError
from flask import request

from models.department import Department
from service.operator import Operator
from rest.schemas.department import DepartmentSchema, DepartmentSearchSchema
from rest.schemas.funcs import lomarsh, marsh_with, marsh_with_field


# pylint: disable=R0201
class DepartmentsApi(Resource):
    """Contains GET and POST request handlers for department table.

    Given class groups handlers which do not require item's id to
    perform a database request.
    """

    @marsh_with(DepartmentSchema, to_many=True)
    def get(self):
        """Returns filtered list of departments from the db using marshal."""
        try:
            search_params = lomarsh(request.args, DepartmentSearchSchema)
            return Operator.get_all(Department, search_expr=self._get_search_expr(search_params))
        except ValidationError:
            abort(400)

    @marsh_with_field(fields.Integer())
    def post(self):
        """Adds a department to the database.

        Returns:
            Department's id using marshal or
            aborts with 404.
        """

        try:
            raw_data = lomarsh(request.form, DepartmentSchema)
            raw_data['id'] = None
            return Operator.insert(Department(**raw_data))
        except IntegrityError:
            abort(400)

    # pylint: disable=E1101
    def _get_search_expr(self, s_params):
        if s_params.get('name'):
            return (Department.name.like(f'%{s_params.get("name")}%'),)
        return None


class DepartmentApi(Resource):
    """Contains GET (by id), PUT and DELETE request handlers for department table.

    Given class groups handlers which require item's id to
    perform a database request.
    """

    @marsh_with(DepartmentSchema)
    def get(self, id_):
        """Gets a department from the database by the id.

        Returns:
            Retreived department using marshal or
            aborts with 404 if department was not present.
        """

        entity = Operator.get_by_id(Department, id_)
        return entity if entity else abort(404)

    @marsh_with_field(fields.Boolean())
    def put(self, id_):
        """Updates a department from the database by the id.

        Returns:
            True (if the operation was successful)
            or False using marshal or aborts with
            code 400.
        """

        try:
            raw_data = lomarsh(request.form, DepartmentSchema)
            raw_data['id'] = id_
            return Operator.update(Department, raw_data)
        except (IntegrityError, ValidationError):
            abort(400)

    # pylint: disable=R1710
    @marsh_with(DepartmentSchema, to_many=True)
    def delete(self, id_):
        """Deletes a department from the database by the id.

        Returns:
            All the departments from the db using marshal or
            aborts with 404 code.
        """

        if Operator.remove(Department, id_):
            return Operator.get_all(Department)
        abort(404)
