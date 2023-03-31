programming = {
	'test': 'sms', 
	'color': 'green', 
	'points': 5
	}

print(programming['color'])
print(programming['test'])
print(programming)

programming['new'] = 'yes'
programming['new2'] = 'yes-yes'
print(programming)


games = {}
games['first'] = 'gta'
games['second'] = 'minecraft'
print(games)
games['first'] = 'minecraft'
games['second'] = 'gta'
print(games)

if games['first'] == 'minecraft':
	print('gogogo')
else:
	print(games['first'])

del programming['new2']
print(programming)



for key, value in games.items():
	print("\nKey: " + key)
	print("Value: " + value)


for name in programming.keys():
	print(name.title())


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" Hi " + name.title() +
		", I see your favorite language is " +
		favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")



for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")


for language in favorite_languages.values():
	print(language.title())


for language in set(favorite_languages.values()):
	print(language.title())