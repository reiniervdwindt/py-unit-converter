from pyunits.units import Unit


class Mass(Unit):
    pass


class Mcg(Mass):
    """
    Microgram (µg or mcg)
    """
    factor = 1e-9


class Mg(Mass):
    """
    Milligram (mg)
    """
    factor = 1e-6


class G(Mass):
    """
    Gram (g)
    """
    factor = .001


class Oz(Mass):
    """
    Ounce (oz)
    """
    factor = .028349523125


class Lb(Mass):
    """
    Pound (lb)
    """
    factor = .45359237


class Kg(Mass):
    """
    Kilogram (kg)
    """
    factor = 1


class St(Mass):
    """
    Stone (st)
    """
    factor = 6.35029318


class CwtUSA(Mass):
    """
    Hundredweight (cwt, short, USA)
    """
    factor = 45.359237


class CwtUK(Mass):
    """
    Hundredweight (cwt, long, UK)
    """
    factor = 50.80234544


class TonUSA(Mass):
    """
    Ton (ton, short, USA)
    """
    factor = 907.18474


class TonMetric(Mass):
    """
    Tonne (t, metric)
    """
    factor = 1e3


class TonUK(Mass):
    """
    Ton (ton, long, UK)
    """
    factor = 1016.0469088


class KtUSA(Mass):
    """
    Kiloton (kt, short, USA)
    """
    factor = 907184.74


class KtMetric(Mass):
    """
    Kilotonne (kt, metric)
    """
    factor = 1e6


class KtUK(Mass):
    """
    Kiloton (kt, long, UK)
    """
    factor = 1016046.9088


class MtUSA(Mass):
    """
    Megaton (Mt, short, USA)
    """
    factor = 907184740


class MtMetric(Mass):
    """
    Megatonne (Mt, metric)
    """
    factor = 1e9


class MtUK(Mass):
    """
    Megaton (Mt, long, UK)
    """
    factor = 1016046908.8
