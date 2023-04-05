class User():
	"""Первый мой класс работника"""

	def __init__(self, name, age):
		"""Инициализация работника"""
		self.name = name
		self.age = age
		self.work = []

	def add_work(self, working):
		"""Добавление работы работнику"""
		self.work.append(working)
		print(f"Работта добавленна - {working}")

	def del_work(self, working):
		"""Удалеине работы работника"""
		if working in self.work:
			self.work.remove(working)
			print(f"Работа удалена - {working}")
		else:
			print("Такой работы нет в списке. \nВот все работы данного работника")
			print(self.work)

	def all_work(self):
		"""Вывод всего списка работ"""
		print("Вот все работы данного работника")
		print(self.work)


new_user = User('romanov', 27)
new_user.all_work()
new_user.add_work('pc')
new_user.add_work('test')
new_user.add_work('pyhton')
new_user.all_work()

new_user.del_work('test')
new_user.del_work('pc2')

print("---")

new_user2 = User('test2', 65)
new_user2.all_work()
new_user2.add_work('text')
new_user2.add_work('read')
new_user2.add_work('write')
new_user2.all_work()

new_user2.del_work('text')
new_user2.del_work('write')
new_user2.all_work()