num_step = 1
while num_step <= 5:
	print(num_step)
	num_step += 1



message = ""

while message != 'q':
	message = input('Your mes 1: ')
	if message != 'q':
		print(message)


active = True
while active:
	message = input('Your mes 2: ')
	if message == 'q':
		active = False
	else:
		print(message)



while True:
	message = input('Your mes 3: ')
	if message == 'q':
		break
	else:
		print(message)



num_step = 0
while num_step < 10:
	num_step += 1
	if num_step % 2 == 0:
		continue
	print(num_step)
	
