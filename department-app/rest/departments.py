from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from flask_restful import Resource, reqparse

from models.department import Department
from service.operator import Operator
from rest.json_response import data_response, error_response

parser = reqparse.RequestParser()


class DepartmentsApi(Resource):
    def get(self):
        departments = Operator.get_all(Department)
        return data_response(Department.json_list(departments))

    def post(self):
        parser.add_argument('name', type=str)
        try:
            raw_data = parser.parse_args()
            department = Department(name=raw_data['name'])
            Operator.insert(department)
            return data_response(department.json())
        except IntegrityError:
            return error_response(404)


class DepartmentApi(Resource):
    def get(self, id):
        try:
            department = Operator.get_by_id(Department, id)
            return data_response(department.json())
        except AttributeError:
            return error_response(404)

    def put(self, id):
        parser.add_argument('id', type=int)
        parser.add_argument('name', type=str)
        try:
            raw_data = parser.parse_args()
            return data_response(Operator.update(Department, raw_data))
        except IntegrityError:
            return error_response(400)

    def delete(self, id):
        try:
            Operator.remove(Department, id)
            return data_response(Department.json_list(Operator.get_all(Department)))
        except UnmappedInstanceError:
            return error_response(404)
