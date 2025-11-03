class WizCoinException(Exception):
    pass


class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        self._galleons = galleons
        self._sickles = sickles
        self._knuts = knuts

    def value(self):
        return (self._galleons * 17 * 29) + (self._sickles * 29) + (self._knuts)

    def weightInGrams(self):
        return (self._galleons * 31.103) + (self._sickles * 11.34) + (self._knuts * 5.0)

    @property
    def galleons(self):
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise f"galleons attr must be set to an int, not a {value.__class__.__qualname__}"
        if value < 0:
            raise f"galleons attr must be a positive int, not a {value.__class__.__qualname__}"
        self._galleons = value

    @property
    def sickles(self):
        return self._sickles

    @sickles.setter
    def sickles(self, value):
        if not isinstance(value, int):
            raise f"sickles attr must be set to an int, not a {value.__class__.__qualname__}"
        if value < 0:
            raise f"sickles attr must be a positive int, not a {value.__class__.__qualname__}"
        self._sickles = value

    @property
    def knuts(self):
        return self._knuts

    @knuts.setter
    def knuts(self, value):
        if not isinstance(value, int):
            raise f"knuts attr must be set to an int, not a {value.__class__.__qualname__}"
        if value < 0:
            raise f"knuts attr must be a positive int, not a {value.__class__.__qualname__}"
        self._knuts = value
