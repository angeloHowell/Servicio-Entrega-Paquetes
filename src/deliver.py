from package import Package

from overweightPackage import OverweightPackage

from person import Person

"""
gives access to class Person
"""
from address import Address

"""
gives access to class Address
"""


class Deliver(object):
    """
    class used to represent a Delivery
    """

    def __init__(self, id_deliver: int = 0, date=None, time=None, sender: Person = Person(),
                 receiver: Person = Person(), sender_add: Address = Address(), receiver_add: Address = Address(),
                 contact: Person = Person(), item: Package = Package()):
        """
        Deliver constructor object
        """
        if time is None:
            time = [0, 0]
        if date is None:
            date = [1, 1, 1999]
        self._id_deliver = id_deliver
        self._date = date
        self._time = time
        self._sender = sender
        self._receiver = receiver
        self._sender_add = sender_add
        self._receiver_add = receiver_add
        self._contact = contact
        self._item = item

    @property
    def id_deliver(self) -> int:
        """ returns id of deliver
            :returns: id_deliver
            :rtype: int
        """
        return self._id_deliver

    @id_deliver.setter
    def id_deliver(self, id_deliver: int):
        """ id of the delivery
            :param id_deliver: id of deliver
            :type: int
        """
        self._id_deliver = id_deliver

    @property
    def date(self):
        """ returns date of deliver
            :returns: date
            :rtype: list
        """
        return self._date

    @date.setter
    def date(self, date):
        """ date of the delivery
            :param date: date of deliver
            :type: list
        """
        self._date = date

    @property
    def time(self):
        """ returns time of deliver
            :returns: time
            :rtype: list
        """
        return self._time

    @time.setter
    def time(self, time):
        """ time of the delivery
            :param time: time of deliver
            :type: list
        """
        self._time = time

    @property
    def sender(self) -> Person:
        """ returns sender of deliver
            :returns: sender
            :rtype: Person
        """
        return self._sender

    @sender.setter
    def sender(self, sender: Person):
        """ sender of the delivery
            :param sender: person who sends the delivery
            :type: Person
        """
        self._sender = sender

    @property
    def receiver(self) -> Person:
        """ returns receiver of deliver
            :returns: deliver
            :rtype: Person
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver: Person):
        """ receiver of the delivery
            :param receiver: person who receives the delivery
            :type: Person
        """
        self._receiver = receiver

    @property
    def sender_add(self) -> Address:
        """ returns address of sender
            :returns: sender_add
            :rtype: Address
        """
        return self._sender_add

    @sender_add.setter
    def sender_add(self, sender_add: Address):
        """ address of the sender of the delivery
            :param sender_add: address of the person who sends the delivery
            :type: Address
        """
        self._sender_add = sender_add

    @property
    def receiver_add(self) -> Address:
        """ returns address of receiver
            :returns: receiver_add
            :rtype: Address
        """
        return self._receiver_add

    @receiver_add.setter
    def receiver_add(self, receiver_add: Address):
        """ address of the receiver of the delivery
            :param receiver_add: address of the person who receives the delivery:
            :type: Address
        """
        self._receiver_add = receiver_add

    @property
    def contact(self) -> Person:
        """ returns person who can be contacted to receive the delivery
            :returns: contact
            :rtype: Person
        """
        return self._contact

    @contact.setter
    def contact(self, contact: Person):
        """ contact of the delivery
            :param contact: person who can be contacted to receive the delivery
            :type: Person
        """
        self._contact = contact

    @property
    def item(self) -> Package:
        """ returns the item of Deliver
            :returns: item
            :rtype: Package
        """
        return self._item

    @item.setter
    def item(self, item: Package):
        """ item of the delivery
            :param item: package that is being sent in the delivery
            :type: Package
        """
        self._item = item

    def __str__(self) -> str:
        """ returns str of deliver
            :returns: string deliver
            :rtype: str
        """

        return 'id = ({0})\ndate = ({1})\nhour = ({2})\nsender = ({3})\nreceiver = ({4})\nsender address = ({5})\n' \
               'receiver address = ({6})\ncontact = ({7})\npackage = ({8})'.format(self._id_deliver, self._date,
                                                                                   self._time, self._sender,
                                                                                   self._receiver, self._sender_add,
                                                                                   self._receiver_add, self._contact,
                                                                                   self._item)

    def __eq__(self, other: 'Deliver') -> bool:
        """ returns boolean value of equivalence between two deliveries
            :param other: another person to compare
            :type: deliver
            :returns: true or false
            :rtype: bool
        """
        if isinstance(other, Deliver):
            return self._id_deliver == other._id_deliver and self._date == other._date and self._time == other._time \
                and self._sender == other._sender and self._receiver == other._receiver and self._sender_add == \
                other._sender_add and self._receiver_add == other._receiver_add and self._contact == other._contact \
                and self._item == other._item
        else:
            return False


if __name__ == '__main__':

    # Empty object
    Empty_Deliver = Deliver()
    print(Empty_Deliver)

    # Object with custom parameters
    New_Deliver = Deliver(45, [21, 3, 2023], [6, 0], Person('123456789', 'TestName1', 'TestLastName1', '300000000'),
                          Person('987654321', 'TestName2', 'TestLastName2', '2000000000'),
                          Address(5, 'TestCity1', 'TestNeighborhood1', 'TestStreet1', 'TestAddressNumber1'),
                          Address(10, 'TestCity2', 'TestNeighborhood2', 'TestStreet2', 'TestAddressNumber2'),
                          Person('30', 'TestContactName', 'TestContactLastName', '1000000000'),
                          OverweightPackage(1, 50, 'whatever a package may have lol'))
    print(New_Deliver)

    # Equality between persons
    AnotherEmptyDeliver = Deliver()
    if Empty_Deliver == AnotherEmptyDeliver:
        print('These deliveries are the same')
    else:
        print('These deliveries are not the same')
