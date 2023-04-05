class UserAge():
	"""Клас для вывода имени юзера"""
	def __init__(self, age = 0):
		self.age = age

	def print_fio(self):
		print(str("Ваш возраст - " + self.age))

	def update_age(self, new_age):
		self.age = new_age
		print("Возраст обновлен")
		