"""Provides user with Department class.

Exported classes:
    Department: ORM representation for 'department' table in the database.

Exported constants:
    MIN_SALARY: Declares minimal salary for an employee.
    MAX_SALARY: Declares max salary for an employee.
"""

from faker import Faker
from faker.providers import date_time

from extensions import db
from models.utility.jsonserializer import JsonSerializer
from models.utility.randomizer import Randomizer
from models.department import Department
from service.operator import Operator

MIN_SALARY = 500
MAX_SALARY = 10000


class Employee(db.Model, JsonSerializer, Randomizer):
    """ORM representation for 'employee' table in the database.

    This class is, basically, a relation schema for 'employee'
    table. An instance of the class represents a row in the table.

    Attributes:
        name: A string corresponding to employee's name.
        birthdate: A date object representing employee's birthdate.
        salary: An integer representing employee's salary.
        department_id: An integer id of the department where employee works.
    """

    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey(
        'department.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.Date)
    salary = db.Column(db.Integer, nullable=False)

    @classmethod
    def random(cls):
        """Generates a random instance of the class.

        Returns:
            An instance of the class with randomly generated
            attributes.
        """
        fake = Faker()
        fake.add_provider(date_time)
        return Employee(
            name=fake.name(),
            birthdate=fake.date_between(start_date='-50y', end_date='-18y'),
            salary=fake.random_int(MIN_SALARY, MAX_SALARY, step=1),
            department_id=fake.random_element(elements=tuple(
                d.id for d in Operator.get_all(Department)))
        )

    def __repr__(self):
        return f'<Employee {self.name}>'
