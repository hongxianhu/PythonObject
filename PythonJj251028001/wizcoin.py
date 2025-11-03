class WizCoinException(Exception):
    pass


class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        self._galleons = galleons
        self._sickles = sickles
        self._knuts = knuts

    @property
    def value(self):
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    @property
    def weightInGrams(self):
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

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

    def __repr__(self):
        return f"{self.__class__.__qualname__}({self.galleons},{self.sickles},{self.knuts})"

    def __str__(self):
        return f"{self.galleons}g,{self.sickles}s,{self.knuts}k"

    def __add__(self, other):
        if not isinstance(other, WizCoin):
            return NotImplemented
        return WizCoin(
            self.galleons + other.galleons,
            self.sickles + other.sickles,
            self.knuts + other.knuts,
        )

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise WizCoinException("connot multiply with negative integers")
        return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        if not isinstance(other, WizCoin):
            return NotImplemented
        return WizCoin(
            self.galleons - other.galleons,
            self.sickles - other.sickles,
            self.knuts - other.knuts,
        )

    def __pow__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return WizCoin(self.galleons**other, self.sickles**other, self.knuts**other)

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)

    def __bool__(self):
        return self.value != 0

    def __iadd__(self, other):
        if not isinstance(other, WizCoin):
            return NotImplemented
        self.galleons += other.galleons
        self.sickles += other.sickles
        self.knuts += other.knuts
        return self

    def __imul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise WizCoinException("cannot multiply with negative integers")
        self.galleons *= other
        self.sickles *= other
        self.knuts *= other
        return self
