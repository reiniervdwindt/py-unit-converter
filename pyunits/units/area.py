from pyunits.units import Unit


class Area(Unit):
    pass


class Sqnm(Area):
    """
    Sq Nanometers
    """
    factor = 1e-18


class Sqmicron(Area):
    """
    Sq Micrometers
    """
    factor = 1e-12


class Sqmm(Area):
    """
    Sq Millimeters
    """
    factor = 1e-6


class Sqcm(Area):
    """
    Sq Centimeters
    """
    factor = 1e-4


class Sqin(Area):
    """
    Sq Inches
    """
    factor = 64516e-8


class Sqft(Area):
    """
    Sq Feet
    """
    factor = .09290304


class Sqyd(Area):
    """
    Sq Yards
    """
    factor = .83612736


class Sqm(Area):
    """
    Sq Meters
    """
    factor = 1


class Ac(Area):
    """
    Acre
    """
    factor = 4046.8564224


class Ha(Area):
    """
    Hectares
    """
    factor = 1e4


class Sqkm(Area):
    """
    Sq Kilometers
    """
    factor = 1e6


class Sqmi(Area):
    """
    Sq Miles
    """
    factor = 2589988.110336


class Sqnmi(Area):
    """
    Sq Nautical Miles
    """
    factor = 3429904
