# Superclass
class Vehicle:
    def move(self):
        pass  # This method will be overridden by subclasses

# Subclass 1
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Main program to demonstrate polymorphism
if __name__ == "__main__":
    car = Car()
    plane = Plane()

    car.move()
    plane.move()
