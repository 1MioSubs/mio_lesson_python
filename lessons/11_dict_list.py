car_1 = {
	'engin': 'gas',
	'color': 'green',
	'km': 1234
}
car_2 = {
	'engin': 'gas',
	'color': 'blue',
	'km': 124
}
car_3 = {
	'engin': 'electro',
	'color': 'green',
	'km': 5234
}

cars = [car_1, car_2, car_3]

for car in cars:
	print(car)


new_cars = []
for car_number in range(30):
	new_car = {
		'engin': 'eqv',
		'color': 'eqv',
		'km': 0
	}
	new_cars.append(new_car)

for new_car in new_cars[:3]:
	if new_car['engin'] == 'eqv':
		new_car['engin'] = 'gas'
		new_car['color'] = 'green'
		new_car['km'] = 2654

for new_car in new_cars[:6]:
	print(new_car)
print("...")




pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " + 
	"with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)


favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}


for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")

	for language in languages:
		print("-\t---" + language.title())



users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
	},
}


for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())