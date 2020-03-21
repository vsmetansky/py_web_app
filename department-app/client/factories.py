"""Provides user with factory functions for application creation.

Exported functions:
    create_app: Creates a Flask application for production purposes.
    create_test_app: Creates a Flask application for testing purposes.
"""

from flask import Flask


def create_app():
    """Creates and configures a Flask app for production.

    Returns:
        An instance of Flask class.
    """

    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG')

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
