from pyunits.units import Unit
from pyunits.units.length import Km, Length, Mi
from pyunits.units.time import Hr, Time


class Speed(Unit):
    distance_class = None
    time_class = None

    def __init__(self, value=1):
        super(Unit, self).__init__()
        self.factored_value = self.distance_class(value) / self.time_class()


def speed_factory(distance_class: type(Length), time_class: type(Time), name='Speed') -> type(Speed):
    return type(name, (Speed,), {
        'distance_class': distance_class,
        'time_class': time_class,
    })


Kph = speed_factory(Km, Hr, 'Kph')
Mph = speed_factory(Mi, Hr, 'Mph')
