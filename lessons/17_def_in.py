def make_new_list(*list_def):
	"""Выводит список полностью"""
	print(list_def)


def make_new_list2(*list_def):
	"""Выводит список полностью"""
	print("full list len:")
	for top in list_def:
		print('--' + top)


def make_new_list3(num_list, *list_def):
	"""Выводит список полностью"""
	print(f"{num_list} - full list len:")
	for top in list_def:
		print('--' + top)


def build_profile(first, last, **user_info):
	"""Строит словарь с информацией о пользователе."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile


if __name__ == '__main__':
	test = 'test'
	print(test)

	#make_new_list('python')
	#make_new_list('python', 'c', 'java')

	#make_new_list2('python')
	#make_new_list2('python', 'c', 'java')

	#make_new_list3(1, 'python')
	#make_new_list3(3, 'python', 'c', 'java')

	user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics', test_name = 'roman')
	print(user_profile)