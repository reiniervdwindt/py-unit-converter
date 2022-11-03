from pyunits.units import Unit


class Time(Unit):
    pass


class Asec(Time):
    """
    Attoseconds
    """
    factor = 1e-18


class Fsec(Time):
    """
    Femtoseconds
    """
    factor = 1e-15


class Psec(Time):
    """
    Picoseconds
    """
    factor = 1e-12


class Nsec(Time):
    """
    Nanoseconds
    """
    factor = 1e-9


class Mcsec(Time):
    """
    Microseconds
    """
    factor = 1e-6


class Msec(Time):
    """
    Milliseconds
    """
    factor = .001


class Sec(Time):
    """
    Seconds
    """
    factor = 1


class Min(Time):
    """
    Minutes
    """
    factor = 60


class Hr(Time):
    """
    Hours
    """
    factor = 3600


class Day(Time):
    """
    Days
    """
    factor = 86400


class Wk(Time):
    """
    Weeks
    """
    factor = 604800


class Mth(Time):
    """
    Months
    """
    factor = 2629746


class Yr(Time):
    """
    Years
    """
    factor = 31556952
