class ElectricCar:
    def __init__(self, battery):
        self.battery = battery

    def drive(self, distance):
        if self.battery == 0:
            return 0
        elif self.battery <= distance and self.battery > 0:
            rest = self.battery
            self.battery = 0
            return rest
        else:
            self.battery -= distance
            return distance

    def charge(self):
        self.battery = 100

def test_electric():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(50) == 0

    car.charge()
    assert car.drive(50) == 50
    assert car.drive(30) == 30
    assert car.drive(50) == 20
    assert car.drive(10) == 0