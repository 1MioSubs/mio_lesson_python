def greet_user():
	"""Выводит простое приведствие"""
	print("Hello!")


def greet_user_2(user):
	"""Выводит приведствиес именем"""
	print("Hello " + user.title() + "!")


def decribe_chanel(what_ser, name_chanel):
	"""Выводит описание сервиса пользователя"""
	print("\nI have a " + what_ser + ".")
	print("My " + what_ser + " chanel name is " + name_chanel + ".")


def decribe_chanel_set(name_chanel, what_ser = 'YouTube'):
	"""Выводит описание сервиса пользователя"""
	print("\nI have a " + what_ser + ".")
	print("My " + what_ser + " chanel name is " + name_chanel + ".")


if __name__ == '__main__':
	#greet_user()

	#username = input('Your name: ')
	#greet_user_2(username)

	#decribe_chanel('youtube', '1MioSubs')
	#decribe_chanel(what_ser = 'twitch', name_chanel = '1MioSubs')

	#decribe_chanel_set(name_chanel = '1MioSubs')
	#decribe_chanel_set('1MioSubs')