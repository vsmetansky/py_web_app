"""Provides user with Department class.

Exported classes:
1. Department (ORM representation for 'department' table in a database).
"""
from faker import Faker

from extensions import db
from .jsonserializer import JsonSerializer
from .randomizer import Randomizer

NAME_MAX_LEN = 50
FAKE = Faker()

class Department(db.Model, JsonSerializer, Randomizer):
    """ORM representation for 'department' table in a database."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(NAME_MAX_LEN), nullable=False)

    @classmethod
    def random(cls):
        return Department(
            name=FAKE.name()
        )

    def __repr__(self):
        return f'<Department {self.name}>'
