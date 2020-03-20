"""Provides user with factory functions for application creation.

Exported functions:
    create_app: Creates a Flask application for production purposes.
    create_test_app: Creates a Flask application for testing purposes.
"""

from flask import Flask

from rest.departments import DepartmentApi, DepartmentsApi
from rest.employees import EmployeeApi, EmployeesApi
from extensions import API, DB, MIGRATE


def add_resources(api):
    """Adds resources to REST application programming interface."""

    api.add_resource(DepartmentsApi, '/departments')
    api.add_resource(DepartmentApi, '/departments/<int:id>')
    api.add_resource(EmployeesApi, '/employees')
    api.add_resource(EmployeeApi, '/employees/<int:id>')


def create_app():
    """Creates and configures a Flask app for production.

    Returns:
        An instance of Flask class with configured database,
        REST resources and migrations.
    """

    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG')

    add_resources(API)

    DB.init_app(app)
    MIGRATE.init_app(app, DB)
    API.init_app(app)

    return app


def create_test_app(api_used=False):
    """Creates and configures a Flask app for testing.

    Returns:
        An instance of Flask class with configured database
        and REST resources.
    """

    app = Flask(__name__)
    app.config.from_envvar('TEST_CONFIG')

    DB.init_app(app)

    if api_used:
        API.resources.clear()
        add_resources(API)
        API.init_app(app)

    return app
