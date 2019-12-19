"""Provides user with Employee class.

Exported classes:
1. Employee (ORM representation for 'employee' table in a database).
"""

from app import DB


class Employee(DB.Model):
    """ORM representation for 'employee' table in a database."""

    id = DB.Column(DB.Integer, primary_key=True)
    department_id = DB.Column(DB.Integer, DB.ForeignKey(
        'department.id'), nullable=False)
    name = DB.Column(DB.String(50), nullable=False)
    birthdate = DB.Column(DB.Date)
    salary = DB.Column(DB.Numeric(12, 4), nullable=False)

    def __repr__(self):
        return f'<Employee {self.name}>'

    def __str__(self):
        return str(self.__dict___)
