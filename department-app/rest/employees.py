from flask_restful import Resource, reqparse
from models.employee import Employee
from service.operator import Operator
import sqlalchemy
from datetime import datetime
from decimal import Decimal


parser = reqparse.RequestParser()


def add_employee_args():
    parser.add_argument('name', type=str)
    parser.add_argument('salary', type=str)
    parser.add_argument('birthdate', type=str)
    parser.add_argument('department_id', type=int)


class EmployeesApi(Resource):
    def get(self):
        employees = Operator.get_all(Employee)
        return {'items': Employee.json_list(employees)}

    def post(self):
        add_employee_args()
        try:
            raw_data = parser.parse_args()
            employee = Employee(name=raw_data['name'], salary=Decimal(raw_data['salary']),
                                birthdate=datetime.strptime(
                                    raw_data['birthdate'], '%Y-%m-%d').date(),
                                department_id=raw_data['department_id'])
            Operator.insert(employee)
            return {'item': employee.json()}
        except sqlalchemy.exc.IntegrityError:
            return {'message': 'Request body is invalid'}, 400


class EmployeeApi(Resource):
    def get(self, id):
        try:
            employee = Operator.get_by_id(Employee, id)
            return {'item': employee.json()}
        except AttributeError:
            return {'message': 'Id does not exist'}, 404

    def put(self, id):
        parser.add_argument('id', type=int)
        add_employee_args()
        try:
            raw_data = parser.parse_args()
            Operator.update(Employee, raw_data)
            return {'item': Operator.get_by_id(Employee, id).json()}
        except sqlalchemy.exc.IntegrityError:
            return {'message': 'Request body is invalid'}, 400

    def delete(self, id):
        try:
            Operator.remove(Employee, id)
            return {'items': Employee.json_list(Operator.get_all(Employee))}
        except sqlalchemy.orm.exc.UnmappedInstanceError:
            return {'message': 'Id does not exist'}, 404
