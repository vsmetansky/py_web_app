"""Contains tests for the 'rest' package."""


import unittest
import random

from flask_restful import marshal

from tests.utility.db_setup import db_init, db_delete
from extensions import DB
from factories import create_test_app
from models.department import Department
from models.employee import Employee
from models.utility.fields import DEPARTMENT_FIELDS, EMPLOYEE_FIELDS


MAX_ENTITY_NUM = 10


class DepartmentsApiTest(unittest.TestCase):
    """A test case for 'rest.departments' module.

    Attributes:
        ctx: An application context.
        client: An application client.
    """

    @classmethod
    def setUpClass(cls):
        cls.app = create_test_app(api_used=True)

    def setUp(self):
        self.ctx = DepartmentsApiTest.app.app_context()
        self.client = DepartmentsApiTest.app.test_client()
        self.ctx.push()
        db_init(DB, (Department,), MAX_ENTITY_NUM)

    def tearDown(self):
        db_delete(DB)
        self.ctx.pop()

    def test_get(self):
        test_entity_id = random.randint(1, MAX_ENTITY_NUM)
        response = self.client.get(f'/departments/{test_entity_id}')
        self.assertIsNotNone(response.get_json().get('data'))

    def test_get_all(self):
        response = self.client.get('/departments')
        self.assertEqual(MAX_ENTITY_NUM,
                         len(response.get_json().get('data')))

    def test_insert(self):
        test_entity = Department.random()
        post_response = self.client.post(
            '/departments', data=marshal(test_entity, DEPARTMENT_FIELDS))

        test_entity_id = post_response.get_json()
        test_entity.id = test_entity_id

        get_response = self.client.get(
            f'/departments/{test_entity.id}')
        get_response_data = get_response.get_json()
        self.assertEqual(marshal(test_entity, DEPARTMENT_FIELDS),
                         marshal(get_response_data, DEPARTMENT_FIELDS))

    def test_delete(self):
        test_entity_id = random.randint(1, MAX_ENTITY_NUM)
        self.client.delete(f'/departments/{test_entity_id}')

        get_response = self.client.get(f'/departments/{test_entity_id}')
        self.assertIsNone(get_response.get_json().get('data'))

    def test_update(self):
        test_entity_new = marshal(Department.random(), DEPARTMENT_FIELDS)

        test_entity_new_id = random.randint(1, MAX_ENTITY_NUM)
        self.client.put(
            f'/departments/{test_entity_new_id}', data=test_entity_new)

        get_response = self.client.get(f'/departments/{test_entity_new_id}')
        test_entity_new['id'] = test_entity_new_id
        self.assertEqual(test_entity_new,
                         get_response.get_json().get('data'))


class EmployeesApiTest(unittest.TestCase):
    """A test case for 'rest.employees' module.

    Attributes:
        ctx: An application context.
        client: An application client.
    """

    @classmethod
    def setUpClass(cls):
        cls.app = create_test_app(api_used=True)

    def setUp(self):
        self.ctx = EmployeesApiTest.app.app_context()
        self.client = EmployeesApiTest.app.test_client()
        self.ctx.push()
        db_init(DB, (Department, Employee), MAX_ENTITY_NUM)

    def tearDown(self):
        db_delete(DB)
        self.ctx.pop()

    def test_get(self):
        test_entity_id = random.randint(1, MAX_ENTITY_NUM)

        response = self.client.get(f'/employees/{test_entity_id}')

        self.assertIsNotNone(response.get_json().get('data'))

    def test_get_all(self):
        response = self.client.get('/employees')

        self.assertEqual(MAX_ENTITY_NUM,
                         len(response.get_json().get('data')))

    def test_insert(self):
        test_entity = Employee.random()
        post_response = self.client.post(
            '/employees', data=marshal(test_entity, EMPLOYEE_FIELDS))

        test_entity_id = post_response.get_json().get('data')
        test_entity.id = test_entity_id

        get_response = self.client.get(
            f'/employees/{test_entity.id}')
        self.assertEqual(marshal(test_entity, EMPLOYEE_FIELDS),
                         get_response.get_json().get('data'))

    def test_delete(self):
        test_entity_id = random.randint(1, MAX_ENTITY_NUM)
        self.client.delete(f'/employees/{test_entity_id}')

        get_response = self.client.get(f'/employees/{test_entity_id}')
        self.assertIsNone(get_response.get_json().get('data'))

    def test_update(self):
        test_entity_new = marshal(Employee.random(), EMPLOYEE_FIELDS)

        test_entity_new_id = random.randint(1, MAX_ENTITY_NUM)
        self.client.put(
            f'/employees/{test_entity_new_id}', data=test_entity_new)

        get_response = self.client.get(f'/employees/{test_entity_new_id}')
        test_entity_new['id'] = test_entity_new_id
        self.assertEqual(test_entity_new,
                         get_response.get_json().get('data'))
