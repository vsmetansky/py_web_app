"""Provides user with factory functions for application creation.

Exported functions:
    create_app: Creates a Flask application for production purposes.
    create_test_app: Creates a Flask application for testing purposes.
"""

from flask import Flask

from views.departments import Departments


def register_routes(app):
    deps_view = Departments.as_view('departments')
    app.add_url_rule('/departments/', methods=('GET',),
                     view_func=deps_view)
    app.add_url_rule('/departments/<int:id_>',
                     view_func=deps_view)


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
