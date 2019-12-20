"""Provides user with Employee class.

Exported classes:
1. Employee (ORM representation for 'employee' table in a database).
"""

from extensions import db
from .jsonserializer import JsonSerializer


class Employee(db.Model, JsonSerializer):
    """ORM representation for 'employee' table in a database."""

    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey(
        'department.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.Date)
    salary = db.Column(db.Numeric(12, 4), nullable=False)

    def __repr__(self):
        return f'<Employee {self.name}>'
