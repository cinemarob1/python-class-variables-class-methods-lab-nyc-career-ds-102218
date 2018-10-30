from collections import Counter

class Driver():
	
	_all = []
	_count = 0

	def __init__(self,name,car_make,car_model):
		self._name = name
		self._car_make = car_make
		self._car_model = car_model
		Driver._all.append(self)
		Driver._count += 1

	@property
	def name(self):
		return self._name
	
	@property
	def car_make(self):
		return self._car_make

	@property
	def car_model(self):
		return self._car_model
	
	@classmethod
	def fleet_size(cls):
		return cls._count

	@classmethod
	def driver_names(cls):
		return [driver.name for driver in cls._all]

	@classmethod
	def fleet_makes(cls):
		return [driver.car_make for driver in cls._all]

	@classmethod
	def fleet_models(cls):
		return [driver.car_model for driver in cls._all]

	@classmethod
	def fleet_makes_count(cls):
		return Counter(cls.fleet_makes())

	@classmethod
	def fleet_models_count(cls):
		return Counter(cls.fleet_models())

	@classmethod
	def percent_of_fleet(cls, make):
		makes_dict = dict(cls.fleet_makes_count())
		percent = makes_dict[make] / cls._count * 100
		return f"{percent}%"



		#######
