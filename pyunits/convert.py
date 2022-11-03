from pyunits.units.area import Area
from pyunits.units.mass import Mass
from pyunits.units.speed import Speed
from pyunits.units.volume import Volume


def area_to_area(area: Area, to: Area) -> Area:
    """
    Convert area from unit to another
    :param area:
    :param to:
    :return:
    """
    return type(to)(area / to)


def mass_to_mass(mass: Mass, to: Mass) -> Mass:
    """
    Convert mass from unit to another
    :param mass:
    :param to:
    :return: float
    """
    return type(to)(mass / to)


def speed_to_speed(speed: Speed, to: Speed) -> Speed:
    """
    Convert speed from unit to another
    :param speed:
    :param to:
    :return:
    """
    return type(to)(speed / to)


def volume_to_volume(volume: Volume, to: Volume) -> Volume:
    """
    Convert volume from unit to another
    :param volume:
    :param to:
    :return:
    """
    return type(to)(volume / to)
