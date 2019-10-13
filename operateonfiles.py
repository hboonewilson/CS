def operateFile(fileName, op):
	'''Open a file and do an operation arguemtent (op) to an already exsisting file'''
	my_file = open(fileName.strip())
	if op.upper() == 'UPPER':
		edit_file = my_file.upper()
	elif op.upper() == 'LOWER':
		edit_file = my_file.lower()
	elif op.upper() == 'TITLE':
		edit_file = my_file.title()
	my_file.close()
	file_output = ('fileName', 'w')
	file_output.write(edit_file)
	file_output.close()

print("Type in the filename and operation to edit the file.")
name = input("File name: ")
op = input("Operation ")
operateFile(name, op)