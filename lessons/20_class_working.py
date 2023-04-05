class Game():
	"""Класс для дредставления игры"""
	def __init__(self, name, platform, year):
		"""Инициализация игры"""
		self.name = name
		self.platform = platform
		self.year = year
		self.min_video = 'gtx1660'


	def get_description_game(self):
		"""Возврашает полную информацию о игре"""
		all_info = str(f"{self.name} - {self.platform} - {self.year}")
		return all_info

	def min_video_cart(self):
		"""Возврашает информацию о минимальных теробованиях к видеокарте"""
		all_info = str(f"Требуется минимально видеокарта - {self.min_video}")
		return all_info

	def update_video_cart(self, video_cart):
		"""Обновляет информацию о минимальных теробованиях к видеокарте"""
		self.min_video = video_cart
		all_info = str(f"Видеокарта обновленна - {video_cart}")
		return all_info


class LocationGame():
	"""Класс локации игры"""
	def __init__(self, location_game):
		"""Инициализация локации проведения игры"""
		self.location_game = location_game

	def local_name(self):
		"""Выводит текущюю локацию игры"""
		print(self.location_game)


class FitGame(Game):
	"""Представляет аспекты для уличных игр"""
	def __init__(self, name, year, min_inventar, platform = "fit_game", location_game = "field"):
		"""Инициализирует атрибуты класса-родителя."""
		super().__init__(name, platform, year)
		self.min_video = min_inventar
		self.location_game = LocationGame(location_game)


	def whate_in_game(self):
		"""Возврашает полную информацию о игре"""
		print(f"В эту игру - {self.name}, нужно играть на - {self.location_game.location_game}")


	def min_video_cart(self):
		"""Возврашает информацию о необходимых вешах"""
		all_info = str(f"Вам понядобится - {self.min_video}")
		return all_info


new_game1 = Game('drive', 2023, 'pc')
print(new_game1.get_description_game())
print(new_game1.min_video_cart())
print(new_game1.update_video_cart('rtx2080'))
print(new_game1.min_video_cart())

print('---')

new_game2 = FitGame('drive', 2023, 'car')
print(new_game2.get_description_game())
new_game2.whate_in_game()
print(new_game2.min_video_cart())
new_game2.location_game.local_name()

print('---')

new_game3 = FitGame('footbool', 2020, 'bool', location_game = "street")
print(new_game3.get_description_game())
new_game3.whate_in_game()
print(new_game3.min_video_cart())
new_game3.location_game.local_name()