from datetime import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from flask_restful import Resource, reqparse

from models.employee import Employee
from service.operator import Operator
from rest.utility.jsonresponse import data_response, error_response

parser = reqparse.RequestParser()


def add_employee_args():
    parser.add_argument('name', type=str)
    parser.add_argument('salary', type=int)
    parser.add_argument('birthdate', type=str)
    parser.add_argument('department_id', type=int)


class EmployeesApi(Resource):
    def get(self):
        employees = Operator.get_all(Employee)
        return data_response(Employee.json_list(employees))

    def post(self):
        add_employee_args()
        try:
            raw_data = parser.parse_args()
            employee = self.__employee_from_raw(raw_data)
            Operator.insert(employee)
            return data_response(employee.json())
        except IntegrityError:
            return error_response(400)

    def __employee_from_raw(self, raw_data):
        return Employee(department_id=raw_data['department_id'],
                        name=raw_data['name'], salary=raw_data['salary'],
                        birthdate=self.__date_from_raw(raw_data['birthdate']))

    def __date_from_raw(self, raw_date):
        return datetime.strptime(raw_date, '%Y-%m-%d').date()


class EmployeeApi(Resource):
    def get(self, id):
        try:
            employee = Operator.get_by_id(Employee, id)
            return data_response(employee.json())
        except AttributeError:
            return error_response(404)

    def put(self, id):
        parser.add_argument('id', type=int)
        add_employee_args()
        try:
            raw_data = parser.parse_args()
            return data_response(Operator.update(Employee, raw_data))
        except IntegrityError:
            return error_response(404)

    def delete(self, id):
        try:
            Operator.remove(Employee, id)
            return data_response(Employee.json_list(Operator.get_all(Employee)))
        except UnmappedInstanceError:
            return error_response(404)
