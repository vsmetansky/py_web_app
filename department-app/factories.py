"""Application's main module. Runs Flask server."""
from flask import Flask

from models import department, employee
from rest.departments import DepartmentApi, DepartmentsApi
from rest.employees import EmployeeApi, EmployeesApi
from extensions import api, db, migrate

def add_resources(api):
    api.add_resource(DepartmentsApi, '/departments')
    api.add_resource(DepartmentApi, '/departments/<int:id>')
    api.add_resource(EmployeesApi, '/employees')
    api.add_resource(EmployeeApi, '/employees/<int:id>')

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG')

    add_resources(api)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    return app

def create_test_app(api_used=False):
    app = Flask(__name__)
    app.config.from_envvar('TEST_CONFIG')

    db.init_app(app)

    if api_used:
        add_resources(api)
        api.init_app(app)

    return app
