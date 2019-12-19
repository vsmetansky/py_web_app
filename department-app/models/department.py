"""Provides user with Department class.

Exported classes:
1. Department (ORM representation for 'department' table in a database).
"""

from app import DB


class Department(DB.Model):
    """ORM representation for 'department' table in a database."""

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50), nullable=False)

    def __repr__(self):
        return f'<Department {self.name}>'

    def __str__(self):
        return str(self.__dict___)
