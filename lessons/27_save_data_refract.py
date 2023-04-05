import json


filename = 'file/data/username.json'

def get_user_storage():
	"""Проверка и получение данных пользователя"""
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except:
		return None
	else:
		return username

def get_new_user():
	"""Создание нового пользователя"""
	username = input('Как вас зовут: ')
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greate_user():
	"""Приведствие пользователя"""
	username = get_user_storage()
	if username:
		print(f"Добро пожаловать обратно - {username}")
	else:
		username = get_new_user()
		print(f"Мы вас запомнили теперь вы не убежите - {username}")

def main():
	greate_user()

if __name__ == "__main__":
	main()