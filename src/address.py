class Address(object):
    """
    class used to represent an Address
    """

    def __init__(self, id_address: int = 0, city: str = 'city', neighborhood: str = 'neighborhood',
                 street: str = 'street', address_num: str = 'addressNum'):
        """
        Address constructor object
        :param id_address: id of address
        :type id_address: int
        :param city: city where the address is
        :type city: str
        :param neighborhood: neighborhood where the address is
        :type neighborhood: str
        :param street: street where the address is
        :type street: str
        :param address_num: number of address
        :type address_num: str
        """
        self._id_address = id_address
        self._city = city
        self._neighborhood = neighborhood
        self._street = street
        self._address_num = address_num

    @property
    def id_address(self) -> int:
        """ returns id of address
            :returns: id_address
            :rtype: str
        """
        return self._id_address

    @id_address.setter
    def id_address(self, id_address: int):
        """ id of address
            :param id_address: id of address
            :type: int
        """
        self._id_address = id_address

    @property
    def city(self) -> str:
        """ returns city where the address is
            :returns: city
            :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """ city of address
            :param city: city where the address is
            :type: str
        """
        self._city = city

    @property
    def neighborhood(self) -> str:
        """ returns neighborhood where the address is
            :returns: neighborhood
            :rtype: str
        """
        return self._neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood: str):
        """ neighborhood of address
            :param neighborhood: neighborhood where the address is
            :type: str
        """
        self._neighborhood = neighborhood

    @property
    def street(self) -> str:
        """ returns street where the address is
            :returns: street
            :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street: str):
        """ street of address
            :param street: street where the address is
            :type: str
        """
        self._street = street

    @property
    def address_num(self) -> str:
        """ returns number of the address
            :returns: address_num
            :rtype: str
        """
        return self._address_num

    @address_num.setter
    def address_num(self, address_num: str):
        """ number of address
            :param address_num: number of address
            :type: str
        """
        self._address_num = address_num

    def __str__(self) -> str:
        """ returns str of address
            :returns: string address
            :rtype: str
        """
        return 'id = {0}, city = ({1}), neighborhood = ({2}), street = ({3}), address number = ({4})'.format(
            self._id_address, self._city, self._neighborhood, self._street, self._address_num)

    def __eq__(self, other: 'Address') -> bool:
        """ returns boolean value of equivalence between two overweight packages
            :param other: another overweight package to compare
            :type: Address
            :returns: true or false
            :rtype: bool
        """
        if isinstance(other, Address):
            return self._id_address == other._id_address and self._city == other._city and self._neighborhood == \
                other._neighborhood and self._street == other._street and self._address_num == other._address_num
        else:
            return False


if __name__ == '__main__':

    # Empty object
    Empty_Address = Address()
    print(Empty_Address)

    # Object with custom parameters
    New_Address = Address(1, 'Gotham City', 'Crime Alley', 'Park Row', '4')
    print(New_Address)

    # Equality between Addresses
    AnotherEmptyAddress = Address()
    if Empty_Address == AnotherEmptyAddress:
        print('These addresses are the same')
    else:
        print('These addresses are not the same')
