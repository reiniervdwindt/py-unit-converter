from unittest import TestCase

from pyunits.calculate import area, average_speed, time_per_area, travel_time
from pyunits.convert import area_to_area, mass_to_mass, speed_to_speed, volume_to_volume
from pyunits.exceptions import InvalidUnitException
from pyunits.units.area import Ac, Ha, Sqft, Sqm, Sqyd
from pyunits.units.length import Ft, In, Km, M, Mi
from pyunits.units.mass import Kg, Lb, Oz
from pyunits.units.speed import Kph, Mph, Speed, speed_factory
from pyunits.units.time import Hr, Min
from pyunits.units.volume import BuUSA, L


class CalculateTestCase(TestCase):
    def test_area(self):
        # Feet to square meters
        result = area(length=Ft(10), width=Ft(20), to=Sqm())
        assert isinstance(result, Sqm)
        assert result == 18.580608

        # Meters to acres
        result = area(length=M(120), width=M(100), to=Ac())
        assert isinstance(result, Ac)
        assert result == 2.965264577605984

    def test_average_speed(self):
        # Miles and time to miles per hour
        result = average_speed(distance=Mi(30), time=Hr(1.25), to=Mph())
        assert isinstance(result, Mph)
        assert result == 24.000000000000004

        # Kilometers and time to kilometers per hour
        result = average_speed(distance=Km(855), time=Hr(10), to=Kph())
        assert isinstance(result, Kph)
        assert result == 85.5

    def test_time_per_area(self):
        # Acres to minutes
        result = time_per_area(area=Ac(10), width=M(12), speed=Kph(10), time=Min())
        assert isinstance(result, Min)
        assert result == 20.234282112000006

        # Sqyd to Hr
        result = time_per_area(area=Sqyd(15), width=In(10), speed=speed_factory(M, Min)(10), time=Hr())
        assert isinstance(result, Hr)
        assert result == 0.08229599999999998

    def test_travel_time(self):
        # Miles and average speed to hours
        result = travel_time(distance=Mi(647), speed=Mph(55), time=Hr())
        assert isinstance(result, Hr)
        assert result == 11.763636363636364

        # Kilometers and average speed to hours
        result = travel_time(distance=Km(855), speed=Kph(100), time=Hr())
        assert isinstance(result, Hr)
        assert result == 8.55


class ConvertTestCase(TestCase):
    def test_convert_area(self):
        # Convert acres to hectares
        result = area_to_area(area=Ac(10), to=Ha())
        assert isinstance(result, Ha)
        assert result == 4.0468564224

        # Convert squared meters to squared feet
        result = area_to_area(area=Sqm(10), to=Sqft())
        assert isinstance(result, Sqft)
        assert result == 107.63910416709722

    def test_convert_speed(self):
        # Convert MPH to KPH using Speed unit
        result = speed_to_speed(speed=Mph(60), to=Kph())
        assert isinstance(result, Kph)
        assert result == 96.56063999999999

        # Convert MPH to KPH using speed factory
        result = speed_to_speed(speed=speed_factory(Mi, Hr)(60), to=Kph())
        assert isinstance(result, Kph)
        assert result == 96.56063999999999

        # Convert KPH to MPH using speed factory
        result = speed_to_speed(speed=Kph(100), to=speed_factory(Mi, Hr)())
        assert isinstance(result, Speed)
        assert result == 62.1371192237334

        # Converting MPH to KPH using to_unit method
        result = Mph(60).to_unit(Kph())
        assert isinstance(result, Kph)
        assert result == 96.56063999999999

        # Converting MPH to KPH using a simple division
        result = Mph(60) / Kph()
        assert isinstance(result, float)
        assert result == 96.56063999999999

    def test_convert_mass(self):
        # KG to LB
        result = mass_to_mass(mass=Kg(10), to=Lb())
        assert isinstance(result, Lb)
        assert result == 22.046226218487757

        # KG to OZ
        result = mass_to_mass(mass=Kg(10), to=Oz())
        assert isinstance(result, Oz)
        assert result == 352.7396194958041

        # LB to KG using to_unit method
        result = Lb(70000).to_unit(Kg())
        assert isinstance(result, Kg)
        assert result == 31751.465900000003

    def test_convert_volume(self):
        # US bushels to liters
        result = volume_to_volume(volume=BuUSA(2000), to=L())
        assert isinstance(result, L)
        assert result == 70478.14

    def test_invalid_unit_exception(self):
        with self.assertRaises(InvalidUnitException):
            Mph(60).to_unit(Lb())
