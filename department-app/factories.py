"""Provides user with factory functions for application creation.

Exported functions:
    create_app: Creates a Flask application for production purposes.
    create_test_app: Creates a Flask application for testing purposes.
"""

from flask import Flask

from rest.departments import DepartmentApi, DepartmentsApi
from rest.employees import EmployeeApi, EmployeesApi
from extensions import api, db, migrate


def add_resources(interface):
    """Adds resources to REST application programming interface."""

    interface.add_resource(DepartmentsApi, '/departments')
    interface.add_resource(DepartmentApi, '/departments/<int:id>')
    interface.add_resource(EmployeesApi, '/employees')
    interface.add_resource(EmployeeApi, '/employees/<int:id>')


def create_app():
    """Creates and configures a Flask app for production.

    Returns:
        An instance of Flask class with configured database,
        REST resources and migrations.
    """

    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG')

    add_resources(api)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    return app


def create_test_app(api_used=False):
    """Creates and configures a Flask app for testing.

    Returns:
        An instance of Flask class with configured database
        and REST resources.
    """

    app = Flask(__name__)
    app.config.from_envvar('TEST_CONFIG')

    db.init_app(app)

    if api_used:
        api.resources.clear()
        add_resources(api)
        api.init_app(app)

    return app
