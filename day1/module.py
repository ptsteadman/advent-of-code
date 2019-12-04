import math


class Module:
    """ Calculates the fuel requirement for a module given its mass.

    >>> a = Module(mass=12)
    >>> a.fuel_requirement()
    2
    >>> b = Module(mass=14)
    >>> b.fuel_requirement()
    2
    >>> c = Module(mass=1969)
    >>> c.fuel_requirement()
    654
    >>> d = Module(mass=100756)
    >>> d.fuel_requirement()
    33583
    """
    def __init__(self, mass):
        self.mass = mass

    def fuel_requirement(self):
        return math.floor(self.mass / 3) - 2
