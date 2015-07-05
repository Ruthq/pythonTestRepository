import verses
B = ""
while (B != "Yes"):
	
	A = input("Would you like to Add a verse or Retrieve a verse? ")

		#if (A == "Add".lower() in A.lower() ):
	if (A == "Add"):
			print(verses.addVerse(input ("book: ") , input ("chapter: ") , input ("verse: ") , input ("verse text: ")))

		#if (A == "Retrieve".lower() in A.lower() ):
	if (A == "Retrieve"):
			print(verses.getRandomVerse())
	B = input("Would you like to end the program? ")




		
	

