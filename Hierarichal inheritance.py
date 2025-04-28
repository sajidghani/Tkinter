class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def show_brand(self):
        print(f'Car__brand: {self.brand}')

class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model

    def show_info(self):
        print(f'Car brand: {self.brand}, Car Model: {self.model}')

class Bike(Vehicle):
    def __init__(self,brand,bike_type):
        super().__init__(brand)
        self.bike = bike_type

    def show_info(self):
        print(f'Bike Brand: {self.brand},Bike type: {self.bike}')

car = Car('Toyota','Corolla')
car.show_info()
bike = Bike('Yamaha','Sport')
bike.show_info()

