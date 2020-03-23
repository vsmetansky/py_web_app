# """Provides models with json serialization options.

# Exported classes:
#     JsonSerializer: A mixin for enabling json serialization for model classes' instances.
# """

# from datetime import date
# from collections import Iterable

# from sqlalchemy.inspection import inspect


# class JsonSerializer:
#     """A mixin for json serialization."""

#     def _json_suitable_val(self, key):
#         val = getattr(self, key)
#         if isinstance(val, date):
#             return str(val)
#         elif isinstance(val, Iterable):
#             return JsonSerializer.json_list(val)
#         return val

#     def json(self):
#         """Creates an object's json representation.

#         Returns:
#             A json serializable dict representation for current object.
#         """
#         return {key: self._json_suitable_val(key) for key in inspect(self).attrs.keys()}

#     @classmethod
#     def json_list(cls, vals):
#         """Creates a list's json representation.

#         Returns:
#             A json serializable representation for given list.
#         """
#         return [val.json() for val in vals]
