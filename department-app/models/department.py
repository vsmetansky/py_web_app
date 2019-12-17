"""Provides user with Department class.

Exported classes:
1. Department (ORM representation for 'department' table in a database).
"""

from flask import g


DB = g.db


class Department(DB.Model):
    """ORM representation for 'department' table in a database."""

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50))

    def __repr__(self):
        return f'<Department {self.name}>'
