import random

class Verse:

	def __init__(self, book, chapter, verse, text):
		self.book = book
		self.chapter = chapter
		self.verse = verse
		self.text = text
		

		
	def toString(self):
		return "\n" + self.book + " " + self.chapter + ":" + self.verse + "\n\t\"" + self.text + "\"\n"
		
	def toFile(self, file):
		file.write("#\n")
		file.write(self.book + "\n")
		file.write(self.chapter + "\n")
		file.write(self.verse + "\n")
		file.write(self.text + "\n")
	
	@classmethod
	def fromFile(clss, file):
		book = file.readline().strip()
		chapter = file.readline().strip()
		verse = file.readline().strip()
		text = file.readline().strip()
		return clss(book, chapter, verse, text)
		

def loadAllVerses():
	verses = []
	verses.append(Verse("Deuteronomy", "28", "12", "The Lord will open to you His good treasure, the heavens, to give the rain to your land in its season, and to bless all the work of your hand. You shall lend to many nations, but you shall not borrow."))
	f = open('verses.txt', 'r')
	for line in f:
		if (line[0] == "#"):
			verses.append(Verse.fromFile(f))
	f.close()
	return verses

def saveAllVerses():
	f = open('verses.txt', 'w')
	#print (verses[0].toString())
	for verse in verseList:
		if (verse.book == "Deuteronomy" and verse.chapter == "28" and verse.verse == "12"):
			continue
		#print(verse.toString())
		verse.toFile(f)
	f.close()
	
def addVerse(book, chapter, verse, verseText):
	verseList.append(Verse(book, chapter, verse, verseText))


def getRandomVerse():
	index = random.randint(0, len(verseList) - 1)
	return verseList[index].toString()
	


verseList = loadAllVerses()

import atexit
atexit.register(saveAllVerses)
#for verse in verseList:
#	print(verse.toString())

#addVerse(str(len(verseList)), str(len(verseList)), str(len(verseList)), str(len(verseList)))
#print (getRandomVerse())
#saveAllVerses(verseList)


	