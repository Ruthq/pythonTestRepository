class Character : 

	def __init__ (self, name, streangth, health, speed):
		self.name = name
		self.streangth = streangth
		self.health = health
		self.speed = speed
	
class Monster(Character) :
	def __init__ (self, name, streangth, health, speed, poision, stealth)
	Character.__init__(self, name, streangth, health, speed)
	self.poision = poision
	self.stealth = stealth

class Player(Character) :
	def __init__ (self, name, streangth, health, speed, inventory,)
	Character.__init__(self, name, streangth, health, speed)
	self.inventory = inventory