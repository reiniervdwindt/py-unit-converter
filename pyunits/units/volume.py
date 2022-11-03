from pyunits.units import Unit


class Volume(Unit):
    pass


class Cunm(Volume):
    """
    Cu nanometers (nm³)
    """
    factor = 1e-27


class Cumicron(Volume):
    """
    Cu micrometers (µm³)
    """
    factor = 1e-18


class Cumm(Volume):
    """
    Cu millimeters (mm³)
    """
    factor = 1e-9


class Cucm(Volume):
    """
    Cu centimeters (cc, cm³)
    """
    factor = 1e-6


class Ml(Volume):
    """
    Milliliters (mL)
    """
    factor = 1e-6


class Cuin(Volume):
    """
    Cu inches (in³)
    """
    factor = 16387064e-12


class FlozImp(Volume):
    """
    Fluid ounces (fl oz, imp)
    """
    factor = 284130625e-13


class FlozUSA(Volume):
    """
    Fluid ounces (fl oz, usa)
    """
    factor = 295735295625e-16


class PtUSA(Volume):
    """
    Pints (pt, usa liq)
    """
    factor = .000473176473


class PtImp(Volume):
    """
    Pints (pt, imp)
    """
    factor = .00056826125


class L(Volume):
    """
    Liters (L)
    """
    factor = .001


class GalUSA(Volume):
    """
    Gallons (gal, usa liq)
    """
    factor = .003785411784


class GalImp(Volume):
    """
    Gallons (gal, imp)
    """
    factor = .00454609


class Cuft(Volume):
    """
    Cu feet (ft³)
    """
    factor = .028316846592


class BuUSA(Volume):
    """
    Bushels (USA)
    """
    factor = .03523907


class BuImp(Volume):
    """
    Bushels (Imp)
    """
    factor = .03636872


class Bbloil(Volume):
    """
    Barrels (bbl, oil)
    """
    factor = .158987294928


class Cuyd(Volume):
    """
    Cu yards (yd³)
    """
    factor = .764554857984


class Cum(Volume):
    """
    Cu meters (m³)
    """
    factor = 1


class Kl(Volume):
    """
    Kiloliters (kL)
    """
    factor = 1


class ML(Volume):
    """
    Megaliters (ML)
    """
    factor = 1e3


class Cukm(Volume):
    """
    Cu kilometres (km³)
    """
    factor = 1e9


class Cumi(Volume):
    """
    Cu miles (mi³)
    """
    factor = 4168181825.4405794


class Cunmi(Volume):
    """
    Cu nautical miles (nmi³)
    """
    factor = 6352182208
