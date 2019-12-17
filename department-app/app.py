"""Application's main module. Runs Flask server."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if __name__ == '__main__':
    APP = Flask(__name__)
