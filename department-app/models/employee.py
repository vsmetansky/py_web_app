"""Provides user with Employee class.

Exported classes: 
1. Employee (ORM representation for 'employee' table in a database).
"""

from flask import g

DB = g.db


class Employee(DB.Model):
    """ORM representation for 'employee' table in a database."""

    id = DB.Column(DB.Integer, primary_key=True)
    department_id = DB.Column(DB.Integer, DB.ForeignKey('department.id'))
    name = DB.Column(DB.String(50))
    birthdate = DB.Column(DB.Date)
    salary = DB.Column(DB.Numeric)
