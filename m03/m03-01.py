"""
Write a Python app that has the following classes:
A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
year
make
model
doors (2 or 4)
roof (solid or sun roof).
Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store the data in the attributes above.
The app will then output the data in an easy-to-read and understandable format, such as this:
  Vehicle type: car
  Year: 2022
  Make: Toyota
  Model: Corolla
  Number of doors: 4
  Type of roof: sun roof
"""

class Vehicle():
    def __init__(self, type):
        self.type = type


class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def get_vehicle_info(self):
        print(f"Vehicle type: {self.type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


def create_vehicle():
    type = input("Enter the vehicle type: ")
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors: ")
    roof = input("Enter the type of roof: ")
    return Automobile(type, year, make, model, doors, roof)


# Main app
if __name__ == "__main__":
    print("Welcome to the Vehicle App!")
    vehicle = create_vehicle()
    print("\nVehicle Information:")
    vehicle.get_vehicle_info()

