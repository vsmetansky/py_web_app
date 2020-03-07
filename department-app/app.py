"""Application's main module. Runs Flask server."""
from models import department, employee

from rest.departments import DepartmentApi, DepartmentsApi
from rest.employees import EmployeeApi, EmployeesApi

from extensions import api, db, migrate
from flask import Flask, got_request_exception

# app = Flask(__name__)
# app.config.from_object(Config)
# db.init_app(app)
# migrate.init_app(app, db)

# api.add_resource(DepartmentsApi, '/departments')
# api.add_resource(DepartmentApi, '/departments/<int:id>')
# api.add_resource(EmployeesApi, '/employees')
# api.add_resource(EmployeeApi, '/employees/<int:id>')

# api.init_app(app)
