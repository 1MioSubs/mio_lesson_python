games = ['minecraft', 'cs', 'valheim', 'dota']
for game in games:
	if game == 'cs':
		print(game.upper())
	else:
		print(game.title())

game = 'Minecraft'
print(game == 'minecraft')
print(game == 'Minecraft')
print(game.lower() == 'minecraft')

if game != 'minecraft':
	print('nonono')

if game != 'Minecraft':
	print('nonono')
else:
	print('yes\n')


age = 27
age2 = 20
print(age == 27)
print(age != 27)
print(age < 27)
print(age > 27)
print(age <= 27)
print(age >= 27)
print("---")
print(age >= 27 and age2 >= 20)
print(age >= 27 and age2 >= 27)
print("---")
print(age >= 27 or age2 >= 20)
print(age >= 28 or age2 >= 27)
print("---")
print('minecraft' in games)
print('valorand' in games)


game_test = 'cs'
if game_test in games:
	print('yes - ' + game_test)
else:
	print('no - ' + game_test)


game_test2 = 'cs-2'

if game_test2 not in games:
	print('no - ' + game_test2)

