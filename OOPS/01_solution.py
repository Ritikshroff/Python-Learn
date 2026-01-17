# Create A car Class With Attributes like Brand and Model, then create an instance of that class


class Car:
    # Brand = None
    # modal = None
    # add a class variable to Car that keeps the track of the number of cars created
    total_cars = 0
    
    def __init__(self, user_brand, user_modal):
        self.__brand = user_brand
        self.__modal = user_modal
        Car.total_cars += 1
# add method to the car class that displays the full name of the car (brand and modal)
    def display_info(self):
        print(self.__brand, self.__modal)
        return F"{self.__modal} {self.__brand}"

# modify the car class to encapculate the brand attribute , making it private, and provide a getter method for it
#incapsulation

    def get_brand(self):
        return self.__brand + "!"

    def set_brand(self, brand):
        self.__brand = brand

# Polymorphisam
# Demonstrate ploymorphisa, by defining a method fuel type in both car and electric car classes but with diffrent behavior
    def fuel_type(self):
        return "Petrol or Deasel"

# Add A static method to the car class that return the genral description of the car
# @staticmethod , Method that belong to the class and not to it's instances
# static methods are decorators 
    @staticmethod
    def Genral_discription():
        return "This is a car discriptionsss"

# use the propeerty decorator in the car class to make the model attribute read only.
    @property
    # we can use @property decorator to make the model attribute read only. so that we can't change the value of the model attribute.
    def get_model(self):
        return self.__modal

My_car = Car("Toyota", "Camry")
print(My_car.get_brand())
My_car.set_brand("Hondaaaaaa")
print(My_car.get_model)
My_car.display_info()


my_new_car = Car("Honda", "Civic")
print(my_new_car.get_brand())
print(my_new_car.get_model)
my_new_car.display_info()



# __init__ is constructor
# self is the reference to the current instance of the class


# --------------------**********----------------------
# Inheritance
# create a electric car class taht has addditional attributes like battery size

class ElectricCar(Car):
    def __init__(self, brand, modal, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, modal)

# Polymorphisam
# Demonstrate ploymorphisa, by defining a method fuel type in both car and electric car classes but with diffrent behavior

    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "100KW")
# Demonstarate teh use of isinstance() to check if my_tesla is an instance of ElectricCar
print(isinstance(my_tesla, ElectricCar))
print(isinstance(my_tesla, Car))
print(my_tesla.get_brand())
# print(my_tesla.modal)
# print(my_tesla.battery_size)
# my_tesla.display_info()
print(my_tesla.get_brand())
print(my_tesla.fuel_type())


safari = Car("Toyota", "Safari")
print(safari.fuel_type())
print(Car.total_cars)
# print(safari.Genral_discription())
print(Car.Genral_discription())
print(Car.get_model)




# Create two class battery and engine and let the electric_car class inharit both , demostrating multiple inharitance

class Battery:
    def Batter_info(self):
        return "Battery size is 100KW"

class Engine:
    def Engine_info(self):
        return "Engine size is 2000cc"


class ElectricCar2(Battery, Engine, Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_new_tesla = ElectricCar2("Tesla", "Model S", "100KW")
print(my_new_tesla.Batter_info())
print(my_new_tesla.Engine_info())
print(my_new_tesla.get_brand())