"""Provides user with factory functions for application creation.

Exported functions:
    create_app: Creates a Flask application for production purposes.
    create_test_app: Creates a Flask application for testing purposes.
"""

import os

from flask import Flask

from views.base import Templates
from views.departments import Departments
from views.employees import Employees


API_BASE_URL = os.environ['API_BASE_URL']
DEPARTMENTS_API_URL = f'http://{API_BASE_URL}/departments'
EMPLOYEES_API_URL = f'http://{API_BASE_URL}/employees'


def register_routes(app):
    Departments.register(
        app, 'departments', '/departments/',
        Templates('department.html', 'departments.html'),
        DEPARTMENTS_API_URL)

    Employees.register(
        app, 'employees', '/employees/',
        Templates('employee.html', 'employees.html'),
        EMPLOYEES_API_URL)


def create_app():
    """Creates and configures a Flask app for production.

    Returns:
        An instance of Flask class.
    """

    app = Flask(__name__)
    app.config.from_envvar('CLIENT_CONFIG')

    register_routes(app)

    return app


# def create_test_app(api_used=False):
#     """Creates and configures a Flask app for testing.

#     Returns:
#         An instance of Flask class with configured database
#         and REST resources.
#     """

#     app = Flask(__name__)
#     app.config.from_envvar('TEST_CONFIG')

#     DB.init_app(app)

#     if api_used:
#         API.resources.clear()
#         add_resources(API)
#         API.init_app(app)

#     return app
