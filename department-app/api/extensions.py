"""Provides user with database, api and migration instances.

The module was created to remove cyclic dependencies.

Exported variables:
    db: an instance of SQLAlchemy class.
    migrate: an instance of Migrate class.
    api: an instance of Api class.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api

DB = SQLAlchemy()
MA = Marshmallow()
MIGRATE = Migrate()
API = Api()
