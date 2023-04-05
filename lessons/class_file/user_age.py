class UserAge():
	"""Клас для вывода имени юзера"""
	def __init__(self, age = 0):
		self.age = age

	def print_fio(self):
		"""Клас для вывода имени юзера"""
		print(str("Ваш возраст - " + self.age))

	def update_age(self, new_age):
		"""Клас для вывода имени юзера"""
		self.age = new_age
		print("Возраст обновлен")
		