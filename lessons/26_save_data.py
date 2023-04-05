import json

numbers = [2, 3, 5, 7, 11, 15]

filename = 'file/json_test.json'

#write
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)

#read
with open(filename) as f_obj:
	numbers_j = json.load(f_obj)

print(numbers_j)


#write prob user data

filename = 'file/data/username.json'

try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except:
	username = input('Как вас зовут: ')
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print(f"Мы вас запомнили теперь вы не убежите - {username}")
else:
	print(f"Добро пожаловать обратно - {username}")