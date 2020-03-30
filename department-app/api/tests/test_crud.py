"""Contains tests for the 'operator' module."""

import unittest
import random

from tests.utility.db_setup import db_init, db_delete
from factories import create_test_app
from extensions import DB
from service.operator import Operator
from models.department import Department
from models.employee import Employee
from rest.schemas.department import DepartmentSchema
from rest.schemas.employee import EmployeeSchema
from rest.schemas.funcs import marsh, lomarsh

MAX_ENTITY_NUM = 10


class DepartmentsTest(unittest.TestCase):
    """A test case for an 'operator' module on 'department' table.

    Attributes:
        ctx: An application context.
    """

    @classmethod
    def setUpClass(cls):
        cls.app = create_test_app()

    def setUp(self):
        self.ctx = DepartmentsTest.app.app_context()
        self.ctx.push()
        db_init(DB, (Department, Employee), MAX_ENTITY_NUM)

    def tearDown(self):
        db_delete(DB)
        self.ctx.pop()

    def test_get(self):
        test_entity_id = random.randint(1, MAX_ENTITY_NUM)
        self.assertIsNotNone(Operator.get_by_id(Department, test_entity_id))

    def test_get_all(self):
        self.assertEqual(MAX_ENTITY_NUM,
                         len(Operator.get_all(Department)))

    def test_insert(self):
        test_entity = Department.random()
        test_entity_id = Operator.insert(test_entity)
        self.assertEqual(test_entity,
                         Operator.get_by_id(Department, test_entity_id))

    def test_delete_instance_presence(self):
        test_entity_id = random.randint(1, MAX_ENTITY_NUM)
        Operator.remove(Department, test_entity_id)
        self.assertIsNone(Operator.get_by_id(Department, test_entity_id))

    def test_delete_refs_presence(self):
        test_entity_id = Operator.get_by_id(
            Employee, random.randint(1, MAX_ENTITY_NUM)).department_id
        Operator.remove(Department, test_entity_id)
        self.assertFalse(Employee.query.filter_by(
            department_id=test_entity_id).all())

    def test_update(self):
        test_entity_new = Department.random()
        test_entity_new.id = random.randint(1, MAX_ENTITY_NUM)

        self.assertTrue(Operator.update(Department, marsh(
            vars(test_entity_new), DepartmentSchema)))


class EmployeesTest(unittest.TestCase):
    """A test case for an 'operator' module on 'employee' table.

    Attributes:
        ctx: An application context.
    """

    @classmethod
    def setUpClass(cls):
        cls.app = create_test_app()

    def setUp(self):
        self.ctx = EmployeesTest.app.app_context()
        self.ctx.push()
        db_init(DB, (Department, Employee), MAX_ENTITY_NUM)

    def tearDown(self):
        db_delete(DB)
        self.ctx.pop()

    def test_get(self):
        test_entity_id = random.randint(1, MAX_ENTITY_NUM)
        self.assertIsNotNone(Operator.get_by_id(Employee, test_entity_id))

    def test_get_all(self):
        self.assertEqual(MAX_ENTITY_NUM,
                         len(Operator.get_all(Employee)))

    def test_insert(self):
        test_entity = Employee.random()
        test_entity_id = Operator.insert(test_entity)
        self.assertEqual(test_entity,
                         Operator.get_by_id(Employee, test_entity_id))

    def test_delete_instance_presence(self):
        test_entity_id = random.randint(1, MAX_ENTITY_NUM)
        Operator.remove(Employee, test_entity_id)
        self.assertIsNone(Operator.get_by_id(Employee, test_entity_id))

    def test_delete_ref_presence(self):
        test_entity_id = random.randint(1, MAX_ENTITY_NUM)
        test_entity_ref_id = Operator.get_by_id(
            Employee, test_entity_id).department_id
        Operator.remove(Employee, test_entity_id)
        self.assertIsNotNone(Operator.get_by_id(
            Department, test_entity_ref_id))

    def test_update(self):
        test_entity_new = Employee.random()
        test_entity_new.id = random.randint(1, MAX_ENTITY_NUM)
        Operator.update(Employee, marsh(test_entity_new, EmployeeSchema))
        self.assertEqual(marsh(test_entity_new, EmployeeSchema),
                         marsh(Operator.get_by_id(Employee, test_entity_new.id), EmployeeSchema))
