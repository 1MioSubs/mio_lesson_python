try:
	print(5/2)
	print('Успешное деление')
except ZeroDivisionError:
	print("Попытка поделить на ноль. Не делай так!")
finally:
	print('Выполнение в любом случае')



print("код работает дальше")