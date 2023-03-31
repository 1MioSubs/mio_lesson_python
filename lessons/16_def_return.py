def format_user_name(first_name, last_name):
	"""Форматирует полное имя"""
	full_name = first_name + ' ' + last_name
	return full_name.title()


def format_user_name_full(first_name, last_name, middle_name = ''):
	"""Форматирует полное FIO"""
	if middle_name:
		full_name = first_name + ' ' + last_name + ' ' + middle_name
		return full_name.title()
	else:
		full_name = first_name + ' ' + last_name
		return full_name.title()


def build_person(first_name, last_name):
	"""Возвращает словарь имя фамилия"""
	person = {'first': first_name, 'last': last_name}
	return person


def build_person_full(first_name, last_name, age = ''):
	"""Возвращает словарь имя фамилия"""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person


def while_func():
	"""Цикл для заполнеи фио"""
	active = True
	while active:
		print('Your name:')
		f_name = input('First name: ')
		if f_name == 'q':
			break

		l_name = input('Last name: ')
		if l_name == 'q':
			break

		format_name_user = format_user_name_full(f_name, l_name)
		print(format_name_user)


def greet_user_list(names):
	"""Выводит приведствие для каждого пользователя"""
	for name in names: 
		msg = "hello, " + name.title() + "!"
		print(msg)


def print_models(unprinted_designs, completed_models):
	"""
	Имитирует печать моделей, пока список не станет пустым.
	Каждая модель после печати перемещается в completed_models.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		# Имитация печати модели на 3D-принтере.
		print("Printing model: " + current_design)
		completed_models.append(current_design)


def show_completed_models(completed_models):
	"""Выводит информацию обо всех напечатанных моделях."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)


if __name__ == '__main__':
	#my_name = format_user_name('roman', 'romanov')
	#print(my_name)

	#my_name = format_user_name_full('roman', 'romanov')
	#print(my_name)
	#my_name = format_user_name_full('roman', 'romanov', 'romanovich')
	#print(my_name)
	
	#my_name = build_person('roman', 'romanov')
	#print(my_name)

	#my_name = build_person_full('roman', 'romanov', 27)
	#print(my_name)

	#while_func()

	#names_list = ['jon', 'den', 'viktor']
	#greet_user_list(names_list)

	#unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
	#completed_models = []
	#print_models(unprinted_designs[:], completed_models)
	#show_completed_models(completed_models)
	#print(unprinted_designs)
	#print(completed_models)