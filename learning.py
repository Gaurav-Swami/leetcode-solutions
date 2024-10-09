class Car:
	def __init__(self,brand,model):
		self.brand = brand
		self.model = model

	def full_name(self):
		return f"{self.brand} {self.model}"

class ElectricCar(Car):
	def __init__(self, brand,model,battery_size):
		super().__init__(brand,model)
		self.battery_size = battery_size


	def full_name(self):
		return f"{self.brand} {self.model} "


car_2 = ElectricCar("Tata","Nexon",10)


print(car_2.full_name())


