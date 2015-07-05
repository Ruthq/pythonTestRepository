

L = ""
while (L != "Yes"):
	A = input('Add, Subtract, Divide, or Multiply? ')
	Y = input('Enter number: ')
	Z = input('Enter number: ')
	
	if ('Add'.lower() in A.lower()):
		print (int(Y) + int(Z))

	elif ('Subtract'.lower() in A.lower()): 
		print (int(Y) - int(Z))

	
	elif ('Divide'.lower() in A.lower()):
		print (int(Y) / int(Z))

	
	else:
		print (int(Y) * int(Z))
		L  = input("Would you like to end the program? ")