""""Declares functions and decorators for marshmallowing.

Exported functions:
    lomarsh: Loads schema instance from provided data.
    marsh: Serializes provided data to JSON-like object.
    marsh_with:
    marsh_with_field:
"""

from marshmallow import Schema


def lomarsh(value, schema):
    """Loads schema instance from provided data."""
    return schema().load(value)


def marsh(value, schema, to_many=False):
    """Serializes provided data to JSON-like object."""
    return schema().dump(value, many=to_many)


def marsh_with(schema, to_many=False):
    """Decorator to serialize flask resource return values via schema.

    Returns:
        Wrapper function, that returns a tuple of JSON-like object,
        corresponding to provided schema, and HTTP code.
    """
    def marsh_with_real(func):
        def wrapped(*args, **kwargs):
            return marsh(func(*args, **kwargs), schema, to_many), 200
        return wrapped
    return marsh_with_real


def marsh_with_field(field):
    """Decorator to serialize flask resource return values via field.

    Returns:
        Wrapper function, that returns a tuple of JSON-like object 
        with single 'data' field and HTTP code.
    """

    def marsh_with_field_real(func):
        def wrapped(*args, **kwargs):
            return marsh({'data': func(*args, **kwargs)}, Schema.from_dict({'data': field})), 200
        return wrapped
    return marsh_with_field_real
