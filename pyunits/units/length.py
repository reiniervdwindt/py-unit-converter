from pyunits.units import Unit


class Length(Unit):
    pass


class Nm(Length):
    """
    Nanometers
    """
    factor = 1e-9


class Micron(Length):
    """
    Micrometers
    """
    factor = 1e-6


class Mm(Length):
    """
    Millimeters
    """
    factor = .001


class Cm(Length):
    """
    Centimeters
    """
    factor = .01


class In(Length):
    """
    Inches
    """
    factor = .0254


class Ft(Length):
    """
    Feet
    """
    factor = .3048


class Yd(Length):
    """
    Yards
    """
    factor = .9144


class M(Length):
    """
    Meters
    """
    factor = 1


class Km(Length):
    """
    Kilometers
    """
    factor = 1e3


class Mi(Length):
    """
    Miles
    """
    factor = 1609.344


class Nmi(Length):
    """
    Nautical Miles
    """
    factor = 1852


class Au(Length):
    """
    Astronomical Units
    """
    factor = 149597870700


class Ly(Length):
    """
    Light Years
    """
    factor = 9460730472580800


class Pc(Length):
    """
    Parsecs
    """
    factor = 0x6da012f958ee1c
