from package import Package

"""
gives access to class Package
"""


class OverweightPackage(Package):
    """
    Class used to represent OverweightPackage:
    Subclass of Package
    """
    MIN_WEIGHT = 4.0
    """
    :MIN_WEIGHT: minimum weight for an OverweightPackage (example = 4.0)
    :type MIN_WEIGHT: constant
    """
    PRICE_EXT_WEIGHT = 1.0
    """
    :PRICE_EXT_WEIGHT: price for each extra kilogram of the package (example = 1.0)
    :type: PRICE_EXT_WEIGHT: constant
    """

    def __init__(self, id_package: int = 0, weight: float = 0.0, description: str = 'Description'):
        """
        OverweightPackage constructor object.
        :param id_package: id of overweightPackage
        :type id_package: int
        :param weight: weight of overweightPackage
        :type weight: float
        :param description: description of overweightPackage
        :type description: str
        """
        super().__init__(id_package, weight, description)
        """
        gives access to base class Package attributes
        :param id_package: id of package
        :type id_package: int
        :param weight: weight of package
        :type weight: float
        :param description: description of package
        :type description: str
        """
        self._cost = self.calculate(weight)

    def calculate(self, weight: float):
        """ calculates cost of overweightPackage with the overweight fee per kilogram
            :returns: weight * W_GR_100 + extra_weight * PRICE_EXT_WEIGHT
            :rtype: float
        """
        extra_weight: float = self._weight - self.MIN_WEIGHT
        return (weight * self.W_GR_100) + (extra_weight * self.PRICE_EXT_WEIGHT)

    def __str__(self) -> str:
        """ returns str of overweightPackage
            :returns: string overweight
            :rtype: str
        """
        return 'id, weight, description, cost =({0}, {1}, {2}, {3})'.format(self._id_package, self._weight,
                                                                            self._description, self._cost)

    def __eq__(self, other: 'OverweightPackage') -> bool:
        """ returns boolean value of equivalence between two overweight packages
            :param other: another overweight package to compare
            :type: OverweightPackage
            :returns: true or false
            :rtype: bool
        """
        if isinstance(other, OverweightPackage):
            return self._id_package == other._id_package and self._weight == other._weight and self._description == \
                other._description and self._cost == other._cost
        else:
            return False


if __name__ == '__main__':

    # Empty object
    Empty_Overweight = OverweightPackage()
    print(Empty_Overweight)

    # Object with custom parameters
    New_Standard = OverweightPackage(1, 3, 'random content of a package')
    print(New_Standard)

    # Equality between overweight packages
    AnotherEmptyOverweight = OverweightPackage()
    if Empty_Overweight == AnotherEmptyOverweight:
        print('These are the same package')
    else:
        print('These are not the same packages')
