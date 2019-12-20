from flask_restful import Resource, reqparse
from models.department import Department
from service.operator import Operator
import sqlalchemy

parser = reqparse.RequestParser()


class DepartmentsApi(Resource):
    def get(self):
        departments = Operator.get_all(Department)
        return {'items': Department.json_list(departments)}

    def post(self):
        parser.add_argument('name', type=str)
        try:
            raw_data = parser.parse_args()
            department = Department(name=raw_data['name'])
            Operator.insert(department)
            return {'item': department.json()}
        except sqlalchemy.exc.IntegrityError:
            return {'message': 'Request body is invalid'}, 400


class DepartmentApi(Resource):
    def get(self, id):
        try:
            department = Operator.get_by_id(Department, id)
            return {'item': department.json()}
        except AttributeError:
            return {'message': 'Id does not exist'}, 404

    def put(self, id):
        parser.add_argument('id', type=int)
        parser.add_argument('name', type=str)
        try:
            raw_data = parser.parse_args()
            Operator.update(Department, raw_data)
            return {'item': Operator.get_by_id(Department, id).json()}
        except sqlalchemy.exc.IntegrityError:
            return {'message': 'Request body is invalid'}, 400

    def delete(self, id):
        try:
            Operator.remove(Department, id)
            return {'items': Department.json_list(Operator.get_all(Department))}
        except sqlalchemy.orm.exc.UnmappedInstanceError:
            return {'message': 'Id does not exist'}, 404
