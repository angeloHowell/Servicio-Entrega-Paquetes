from package import Package

"""
gives access to class Package
"""


class StandardPackage(Package):
    """
    Class used to represent StandardPackage:
    Subclass of Package
    """
    FEE = 2.0
    """
    :FEE: set fee for a standardPackage (example = 2.0)
    :type FEE: constant 
    """

    def __init__(self, id_package: int = 0, weight: float = 0.0, description: str = 'Description'):
        """
        StandardPackage constructor object.
        :param id_package: id of standardPackage
        :type id_package: int
        :param weight: weight of standardPackage
        :type weight: float
        :param description: description of standardPackage
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
        """ calculates cost of the standardPackage with the set fee
            :returns: weight * W_GR_100 + FEE
            :rtype: float
        """
        return (weight * self.W_GR_100) + self.FEE

    def __str__(self) -> str:
        """ returns str of standardPackage
            :returns: string standardPackage
            :rtype: str
        """
        return 'id = ({0}), weight = ({1}), description = ({2}), cost =  ({3})'.format(self._id_package, self._weight,
                                                                                       self._description, self._cost)

    def __eq__(self, other: 'StandardPackage') -> bool:
        """ returns boolean value of equivalence between two standard packages
            :param other: another standard package to compare
            :type: StandardPackage
            :returns: true or false
            :rtype: bool
        """
        if isinstance(other, StandardPackage):
            return self._id_package == other._id_package and self._weight == other._weight and self._description == \
                other._description and self._cost == other._cost
        else:
            return False


if __name__ == '__main__':

    # Empty object
    Empty_Standard = StandardPackage()
    print(Empty_Standard)

    # Object with custom parameters
    New_Standard = StandardPackage(1, 3, 'random content of a package')
    print(New_Standard)

    # Equality between standard packages
    AnotherEmptyStandard = StandardPackage()
    if Empty_Standard == AnotherEmptyStandard:
        print('These are the same package')
    else:
        print('These are not the same packages')
