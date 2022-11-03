from pyunits.units.area import Area
from pyunits.units.length import Length
from pyunits.units.speed import Speed
from pyunits.units.time import Time


def area(length: Length, width: Length, to: Area) -> Area:
    """
    Calculate area with length and width
    :param length:
    :param width:
    :param to:
    :return:
    """
    return type(to)(length * width / to)


def average_speed(distance: Length, time: Time, to: Speed) -> Speed:
    """
    Calculate average speed with distance and time
    :param distance:
    :param time:
    :param to:
    :return:
    """
    return type(to)(distance / time / to)


def time_per_area(area: Area, width: Length, speed: Speed, time: Time) -> Time:
    """
    Calculate amount of time to process area
    :param area:
    :param width:
    :param speed:
    :param time:
    :return:
    """
    return type(time)(area / (width * speed) / time)


def travel_time(distance: Length, speed: Speed, time: Time) -> Time:
    """
    Calculate travel time
    :param distance:
    :param speed:
    :param time:
    :return:
    """
    return type(time)(distance / speed / time)
