"""Provides user with Employee class.

Exported classes:
1. Employee (ORM representation for 'employee' table in the database).
"""
from faker import Faker
from faker.providers import date_time

from extensions import db
from .jsonserializer import JsonSerializer
from .randomizer import Randomizer
from service.operator import Operator

MIN_SALARY = 500
MAX_SALARY = 10000
FAKE = Faker()
FAKE.add_provider(date_time)

class Employee(db.Model, JsonSerializer, Randomizer):
    """ORM representation for 'employee' table in the database."""

    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey(
        'department.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.Date)
    salary = db.Column(db.Integer, nullable=False)

    @classmethod
    def random(cls):
        return Employee(
            name=FAKE.name(),
            birthdate=FAKE.date_between(start_date='-50y', end_date='-18y'),
            salary=FAKE.random_int(MIN_SALARY, MAX_SALARY, step=1),
            department_id=FAKE.random_element(elements=tuple(e.id for e in Operator.get_all(Employee)))
        )

    def __repr__(self):
        return f'<Employee {self.name}>'
