from functools import reduce

from pyunits.exceptions import InvalidUnitException


class Unit(float):
    factor = 1
    factored_value = 1

    def __init__(self, value=1):
        super(Unit, self).__init__()
        self.factored_value = float(value) * self.factor

    def __mul__(self, other):
        return reduce(lambda x, y: x * y, self._get_values(self, other))

    def __rtruediv__(self, other):
        return reduce(lambda x, y: y / x, self._get_values(self, other))

    def __truediv__(self, other):
        return reduce(lambda x, y: x / y, self._get_values(self, other))

    @staticmethod
    def _get_values(*values):
        return (value.factored_value if isinstance(value, Unit) else value for value in values)

    def to_unit(self, unit) -> 'Unit':
        if not issubclass(type(unit), self.__class__.__base__):
            raise InvalidUnitException(f'Unit must derive from {type(self)}')
        return type(unit)(self / unit)
