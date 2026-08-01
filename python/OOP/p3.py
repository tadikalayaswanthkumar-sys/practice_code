class Vehicle:  # Base Class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment
        print(f"{self.brand} {self.model} is accelerating. Current speed: {self.speed} km/h")

    def make_sound(self):
        # This method is meant to be overridden by subclasses
        pass

class Car(Vehicle):  # Derived Class
    def __init__(self, brand, model, doors=4):
        super().__init__(brand, model)
        self.doors = doors

    def drive(self):
        print("Driving the car on the road.")

    def make_sound(self):
        # Overriding the base method (Polymorphism)
        return "Vroom Vroom!"

class ElectricBike(Vehicle):  # Derived Class 2
    def ring_bell(self):
        print("Ring! Ring!")

    def make_sound(self):
        # Overriding again
        return "Beep Beep!"

# Example Usage
my_car = Car("Toyota", "Camry", 4)
my_bike = ElectricBike("Tesla", "Model B")

# Demonstrating Encapsulation & Methods
my_car.accelerate(50)  # Updates and prints internal speed

# Demonstrating Polymorphism
# Both objects have the 'make_sound' method but behave differently
for vehicle in [my_car, my_bike]:
    print(f"{vehicle.brand} sound: {vehicle.make_sound()}")