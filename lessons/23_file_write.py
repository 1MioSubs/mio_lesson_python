file_write = "file/my_write.txt"

with open(file_write, 'w') as file:
	file.write("I Love Programming Python!\n")
	file.write("I love creating new games!\n")

with open(file_write, 'a') as file:
	file.write("I also love finding meaning in large datasets.\n")
	file.write("I love creating apps that can run in a browser.\n")