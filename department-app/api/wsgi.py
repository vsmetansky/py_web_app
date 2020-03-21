"""Application's main module that creates Flask application.

The module is used to provide WSGI server with Flask
application's instance.
"""

from factories import create_app

APP = create_app()

if __name__ == '__main__':
    APP.run()
