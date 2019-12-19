from app import DB

"""Provides user with Operator class.

Exported classes:
1. Operator (Class with CRUD methods).
"""


class Operator:
    """Operator class."""

    @classmethod
    def get_all(cls, model):
        return model.query.all()

    @classmethod
    def get_by_id(cls, model, id):
        return model.query.get(id)

    @classmethod
    def add(cls, value):
        DB.session.add(value)
        DB.session.commit()

    @classmethod
    def remove(cls, value):
        DB.session.delete(value)
        DB.session.commit()

    @classmethod
    def update(cls, model, value):
        old_value = model.query.get(value.id)
        old_value = value
        DB.session.commit()
