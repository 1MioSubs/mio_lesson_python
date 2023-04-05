from class_file.user_age import UserAge

class FioUser():
	"""Клас для вывода имени юзера"""
	def __init__(self, f_name, l_name):
		self.f_name = f_name
		self.l_name = l_name
		self.age_info = UserAge()

	def print_fio(self):
		print(str(
			self.f_name.title()) + 
			" " + 
			str(self.l_name.title()) + 
			" Ваш возраст - " + 
			str(self.age_info.age)
			)

	def age_info_update(self, age):
		self.age_info.update_age(age)
		