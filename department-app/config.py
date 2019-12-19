"""Provides user with configuration constants.

Exported constants:
1. SQLALCHEMY_DATABASE_URI (provides user with corresponding flask-sqlalchemy configuration key)
2. SQLALCHEMY_TRACK_MODIFICATIONS (provides user with corresponding flask-sqlalchemy configuration key)
"""


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://vsmet:112358@localhost/deps_emps_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
