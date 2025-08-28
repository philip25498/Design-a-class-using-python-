# Parent class
class Superhero:
    def __init__(self, name, alter_ego, powers):
        self.name = name
        self.alter_ego = alter_ego
        self.powers = powers
        self.is_superhero = True

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Alter Ego: {self.alter_ego}")
        print(f"Powers: {', '.join(self.powers)}")

    def use_power(self, power):
        if power in self.powers:
            print(f"{self.name} uses their {power} power!")
        else:
            print(f"{self.name} does not have the {power} power.")

# Child class demonstrating inheritance and polymorphism
class FlyingSuperhero(Superhero):
    def __init__(self, name, alter_ego, powers, flight_speed):
        super().__init__(name, alter_ego, powers)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at a speed of {self.flight_speed} mph!")

    def display_info(self):
        super().display_info()
        print(f"Flight Speed: {self.flight_speed} mph")

# Create a superhero object
superman = FlyingSuperhero(
    name="Superman",
    alter_ego="Clark Kent",
    powers=["Super strength", "Flight", "Heat vision"],
    flight_speed=2000
)

# Use the methods
superman.display_info()
superman.use_power("Heat vision")
superman.fly()
