my_games = ['mine', 'cs', 'dota', 'nomans']
friend_games = []

while my_games:
	select_my_game = my_games.pop()
	friend_games.append(select_my_game)
	print('Game add my friends: ' + select_my_game.title())

print(my_games)
print('game friend')
for friend_game in friend_games:
	print(friend_game)



my_games = ['mine', 'cs', 'dota', 'cs', 'nomans', 'cs']
print(my_games)

while 'cs' in my_games:
	my_games.remove('cs')

print(my_games)


print("-----------------------")

response = {}

active = True

while active:
	obl = input("where:")
	merg = input("what:")

	response[obl] = merg

	repeat = input("yes/no")
	if repeat == 'no':
		active = False

for obl, merg in response.items():
	print(obl + ': ' + merg)