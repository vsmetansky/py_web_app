"""Provides models with abstract Randomizer class.

Exported classes:
    Randomizer: Gives models an interface for random instance generation.
"""

from abc import abstractmethod


class Randomizer():
    """Gives models an interface for random instance generation.

    This class is an abstract class with a single method, that should
    be overriden by each of the models if random instance generation
    is needed.
    """
    @classmethod
    @abstractmethod
    def random(cls):
        """An abstract class method for random instance generation"""
