"""Provides user with Department class.

Exported classes:
    Department: ORM representation for 'department' table in the database.
"""

from faker import Faker

from extensions import DB
from models.utility.jsonserializer import JsonSerializer
from models.utility.randomizer import Randomizer


class Department(DB.Model, JsonSerializer, Randomizer):
    """ORM representation for 'department' table in the database.

    This class is, basically, a relation schema for 'department'
    table. An instance of the class represents a row in the table.

    Attributes:
        name: A string corresponding to department's name.
    """

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50), nullable=False)

    @classmethod
    def random(cls):
        """Generates a random instance of the class.

        Returns:
            An instance of the class with randomly generated
            attributes.
        """
        return Department(
            name=Faker().name()
        )

    def __repr__(self):
        return f'<Department {self.name}>'
