msg_not = "Такого файла не сушествует"


def num_word(path):
	try:
		with open(path) as file:
			contents = file.read()
	except FileNotFoundError:
		#name = path.split("/")
		#print(name[-1] + ' - ' + msg_not)
		pass
	else:
		words = contents.split()
		num_words = len(words)
		name = path.split("/")
		print(f"Эта книга - {name[-1]}, состоит из - {str(num_words)} слов.")


def main():
	file_path = "file/book/"
	file_names = ['alice.txt', 'siddhartha.txt', 'test.txt', 'moby_dick.txt', 'little_women.txt']
	for file_name in file_names:
		full_path = file_path + file_name
		num_word(full_path)

if __name__ == "__main__":
	main()