favorit_games = ['minecraft', 'nfs', 'dota', 'nier']
for favorit_game in favorit_games:
	print(favorit_game)

for favorit_game in favorit_games:
	print(favorit_game.title() + " - Best Game")



for value in range(1,6):
	print(value)


numbers = list(range(1, 6))
print(numbers)


numbers = list(range(2, 11, 2))
print(numbers)


squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)



digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


squares2 = [value**2 for value in range(1, 11)]
print(squares2)


players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player)




my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods2 = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print("\nMy friend's favorite foods 2 are:")
print(friend_foods2)
