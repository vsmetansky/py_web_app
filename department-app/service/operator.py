"""Provides user with an Operator class.

Exported classes:
    Operator: contains methods to perform CRUD operations.
"""

from extensions import db


class Operator:
    """Contains methods to perform CRUD operations."""

    @classmethod
    def get_all(cls, model):
        """Gets all rows of given model from the database.

        Returns:
            A list of fetched rows in the form of objects.
        """

        return model.query.all()

    @classmethod
    def get_by_id(cls, model, id):
        """Gets one row of given model by the provided id from the database.

        Returns:
            A fetched row in the form of object.
        """

        return model.query.get(id)

    @classmethod
    def insert(cls, value):
        """Inserts given row into the database.

        Returns:
            An integer, representing row's id.
        """

        db.session.add(value)
        db.session.commit()
        return value.id

    @classmethod
    def remove(cls, model, id):
        """Removes a row from the database by the id."""

        model.query.filter_by(id=id).delete()
        db.session.commit()

    @classmethod
    def update(cls, model, upd_data):
        """Updates a row in the database by the id.

        Returns:
            True, if the row was updated, or False
            otherwise.
        """

        old_value = model.query.get(upd_data.get('id'))
        if old_value.get('id'):
            model.query.filter_by(id=old_value['id']).update(upd_data)
            db.session.commit()
            return True
        return False
