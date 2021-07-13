class Car:
    def __init__(self, make, model): # constructor/initializers
        # self allows the properties to be available to the objects
        self.make = ""
        self.model = ""
        self.vin = ""
        self.color = ""
        self.no_of_cylinders = 2
        self.speed = 0
        self.current_gear = "N"

    def drive(self)        :
        print("Car is driving")
        self.current_gear = "D"

    def park(self):
        self.spedd = 0
        self.current_gear = "P"

# when we create an object/instance of a Car class we are using the Car blueprint to represent
# an actual car like Honda, Toyota, Tesla, BMW, etc.

car = Car()
