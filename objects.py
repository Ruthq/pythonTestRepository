class Item:

	someAttribute = "someDefaultValue"
	itemName = ""
	itemSize = 0

	def __init__(self, name, size):
		self.itemName = name
		self.itemSize = size
	
	def increaseSize(self):
		self.itemSize += 1
		
	def forgetMyName():
		self.name = ""
		
	def changeMyNameToStupid():
		self.name = "stupid"
	
	
class ConsumableItem(Item):
	pass

	
class DestructableItem(Item):
	durability = 0
	
	def __init__(self, name, size, durability):
		Item.__init__(self, name, size)
		self.durability = durability
	
class Weapon(DestructableItem):
	damage = 0
	
	def __init__(self, name, size, dmg, durability):
		super().__init__(name, size, durability)
		self.damage = dmg

sword = Weapon("sword", 5, 10, 500)

print (sword.itemName)
print (sword.itemSize)
print (sword.someAttribute)
print (sword.damage)
#print (sword.durability)


