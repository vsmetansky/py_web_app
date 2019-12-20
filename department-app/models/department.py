"""Provides user with Department class.

Exported classes:
1. Department (ORM representation for 'department' table in a database).
"""

from extensions import db
from .jsonserializer import JsonSerializer


class Department(db.Model, JsonSerializer):
    """ORM representation for 'department' table in a database."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Department {self.name}>'
