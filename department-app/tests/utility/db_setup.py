"""Contains functions for DB configuration.

Exported functions:
    db_init: Creates DB tables and fills them with data.
    db_delete: Deletes all of the DB tables.
"""


def db_init(db, models, entity_num):
    """Creates DB tables and fills them with data."""

    db.create_all()
    for m in models:
        db.session.add_all(
            m.random() for _ in range(entity_num)
        )
        db.session.commit()


def db_delete(db):
    """Deletes all of the DB tables."""

    db.session.commit()
    db.drop_all()
