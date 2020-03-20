"""Provides user with the setup configuration."""

from setuptools import setup, find_packages


setup(
    name='DepartmentApp',
    version='0.1',
    packages=find_packages(),
    install_requires=(
        'Flask >= 1.1.1',
        'Flask-Migrate >= 2.5.2',
        'Flask-SQLAlchemy >= 2.4.1',
        'Flask-RESTful >= 0.3.7',
        'PyMySQL >= 0.9.3'
    ),
)
