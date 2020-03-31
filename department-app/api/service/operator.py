"""Provides user with an Operator class.

Exported classes:
    Operator: contains methods to perform CRUD operations.
"""

from copy import copy

from extensions import DB


class Operator:
    """Contains methods to perform CRUD operations."""

    @classmethod
    def get_all(cls, model, search_expr=None, search_args=None):
        """Gets all rows of given model from the database or 
        a list of rows, that corresponds to provided filter.

        Returns:
            A list of fetched rows in the form of objects.
        """

        if search_args:
            return model.query.filter_by(**search_args).all()
        elif search_expr:
            return model.query.filter(*search_expr).all()
        return model.query.all()

    @classmethod
    def get_by_id(cls, model, id_):
        """Gets one row of given model by the provided id from the database.

        Returns:
            A fetched row in the form of object.
        """

        return model.query.get(id_)

    @classmethod
    def insert(cls, value):
        """Inserts given row into the database."""
        DB.session.add(value)
        DB.session.commit()

        return value.id

    @classmethod
    def remove(cls, model, id_):
        """Removes a row from the database by the id."""
        effected_rows = model.query.filter_by(id=id_).delete()
        DB.session.commit()
        return True if effected_rows else False

    @classmethod
    def update(cls, model, upd_data):
        """Updates a row in the database by the id.

        Returns:
            True, if the row was updated, or False
            otherwise.
        """

        effected_rows = model.query.filter_by(
            id=upd_data.get('id')).update(upd_data)
        DB.session.commit()
        return True if effected_rows else False
