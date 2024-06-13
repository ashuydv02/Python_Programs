class vehicle:
    model = ""
    type = ""

    def display_model(self):
        print(vehicle.model)


class car(vehicle):
    def __init__(self, name):
        vehicle.model = name
        vehicle.type = "Car"

    def speed(self, topspeed):
        print(f"Top Speed of {self.model} is {topspeed}")


swift = car("swift")
print(swift.type)
swift.display_model()
swift.speed(150)
