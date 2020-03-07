from extensions import db

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
    def insert(cls, value):
        db.session.add(value)
        db.session.commit()

    @classmethod
    def remove(cls, model, id):
        model.query.filter_by(id=id).delete()
        db.session.commit()

    @classmethod
    def update(cls, model, upd_data):
        old_value = model.query.get(upd_data.get('id'))
        if old_value.get('id'):
            model.query.filter_by(id=old_value['id']).update(upd_data)
            db.session.commit()
