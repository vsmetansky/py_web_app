""""Declares functions and decorators for marshmallowing."""

from marshmallow import Schema


def marsh(value, schema):
    return schema().dump(value)


def marsh_with(schema):
    def marsh_with_real(func):
        def wrapped(*args, **kwargs):
            return marsh(func(*args, **kwargs), schema), 200
        return wrapped
    return marsh_with_real


def marsh_with_field(field):
    def marsh_with_field_real(func):
        def wrapped(*args, **kwargs):
            return marsh({'data': func(*args, **kwargs)}, Schema.from_dict({'data': field})), 200
        return wrapped
    return marsh_with_field_real
