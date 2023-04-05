try:
	print(5/0)
except ZeroDivisionError:
	print("Попытка поделить на ноль. Не делай так!")


print("Дай мне два числа я тебе их поделю: ")
print("Введите 'q' для выхода из цикла!")

while True:
	first_num = input("\nFirst number: ")
	if first_num == "q":
		break
	second_num = input("\nSecond number: ")
	if first_num == "q":
		break
	
	try:
		answer = int(first_num) / int(second_num)
	except ZeroDivisionError:
		print("Попытка поделить на ноль. Не делай так!")
	else:
		print(answer)