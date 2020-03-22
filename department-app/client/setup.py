"""Provides user with the setup configuration."""

from setuptools import setup, find_packages


setup(
    name='DepartmentAppClient',
    version='0.1',
    packages=find_packages(),
    install_requires=(
        'Flask >= 1.1.1'
    ),
)
