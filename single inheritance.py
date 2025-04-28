# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print(f'{self.name} makes a sound.')
#
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed
#     def speak(self):
#         print(f'{self.name} the {self.breed} barks.')
#
# dog = Dog('Buddy','Labrador')
# dog.speak()

#
#

class Vehicle:
    def __init__(self,name,brand,mode):
        self.name = name
        self.brand = brand
        self.mode = mode

    def detail(self):
        print(f'Car_Name:{self.name},Brand: {self.brand},Mode: {self.mode}')

class Car(Vehicle):
    def __init__(self,name,brand,mode,model,car_type):
        super().__init__(name,brand,mode)
        self.model = model
        self.car_type = car_type

    def detail(self):
        print(f'{self.car_type} is the company of {self.brand}, is a {self.mode}, having {self.model} model.')

car1 = Car('Corolla','X','Automatic','2010','Axio')
car1.detail()
car1.d