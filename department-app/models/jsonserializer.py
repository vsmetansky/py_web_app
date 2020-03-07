from sqlalchemy.inspection import inspect

from datetime import date
from decimal import Decimal


class JsonSerializer:
    def _json_suitable_val(self, key):
        val = getattr(self, key)
        if isinstance(val, date):
            return str(val)
        return val

    def json(self):
        return {key: self._json_suitable_val(key) for key in inspect(self).attrs.keys()}

    @classmethod
    def json_list(cls, l):
        return [val.json() for val in l]
