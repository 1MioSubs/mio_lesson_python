file_path = "file/pi_digits.txt"
file_path_milli = "file/pi_million_digits.txt"
file_path2 = r'C:\Users\roman\dev\python\mio_lesson_python\lessons\file\pi_digits.txt'

with open(file_path) as file_object:
	contents = file_object.read()
	print(contents)

print("--- ---")

with open(file_path2) as file:
	contents = file.read()
	print(contents.rstrip())

print("--- ---")

with open(file_path) as file:
	for line in file:
		print(line.rstrip())

print("--- ---")

with open(file_path) as file:
	lines = file.readlines()
	for line in lines:
		print(line.rstrip())

print("--- ---")

with open(file_path) as file:
	lines = file.readlines()

	pi_string = ''
	for line in lines:
		pi_string += line.strip()

	print(pi_string)
	print(len(pi_string))

print("--- ---")

with open(file_path_milli) as file:
	lines = file.readlines()

	pi_string = ''
	for line in lines:
		pi_string += line.strip()

	print(pi_string[:52] + "...")
	print(len(pi_string))

print("--- ---")

with open(file_path_milli) as file:
	lines = file.readlines()

	pi_string = ''
	for line in lines:
		pi_string += line.strip()

	birthday = input("Enter your birthday, in the form mmddyy: ")
	if birthday in pi_string:
		print("Your birthday appears in the first million digits of pi!")
	else:
		print("Your birthday does not appear in the first million digits of pi.")