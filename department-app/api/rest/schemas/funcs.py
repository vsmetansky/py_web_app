""""Declares functions and decorators for marshmallowing."""

from marshmallow import Schema


def lomarsh(value, schema):
    return schema().load(value)


def marsh(value, schema, to_many=False):
    return schema().dump(value, many=to_many)


def marsh_with(schema, to_many=False):
    def marsh_with_real(func):
        def wrapped(*args, **kwargs):
            return marsh(func(*args, **kwargs), schema, to_many), 200
        return wrapped
    return marsh_with_real


def marsh_with_field(field):
    def marsh_with_field_real(func):
        def wrapped(*args, **kwargs):
            return marsh({'data': func(*args, **kwargs)}, Schema.from_dict({'data': field})), 200
        return wrapped
    return marsh_with_field_real
