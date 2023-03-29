from person import Person
from address import Address
from package import Package
from standardPackage import StandardPackage
from overweightPackage import OverweightPackage
from deliver import Deliver

if __name__ == '__main__':
    emptyDeliverTest = Deliver()
    print(emptyDeliverTest)

    DeliverTest = Deliver(45, [21, 3, 2023], [6, 0], Person('123456789', 'TestName1', 'TestLastName1', '300000000'),
                          Person('987654321', 'TestName2', 'TestLastName2', '2000000000'),
                          Address(5, 'TestCity1', 'TestNeighborhood1', 'TestStreet1', 'TestAddressNumber1'),
                          Address(10, 'TestCity2', 'TestNeighborhood2', 'TestStreet2', 'TestAddressNumber2'),
                          Person('30', 'TestContactName', 'TestContactLastName', '1000000000'),
                          OverweightPackage(1, 50, 'whatever'))
    print(DeliverTest)
