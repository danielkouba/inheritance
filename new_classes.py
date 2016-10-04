from human import Human
class Wizard(Human):
	def __init__(self):
		super(Wizard, self).__init__()
		self.intelligence = 10
		print "...with a class Wizard"
	def heal(self):
		self.health += 10
class Ninja(Human):
	def __init__(self):
		super(Ninja, self).__init__()
		self.stealth = 10
		print "...with a class Ninja"
	def steal(self):
		self.stealth += 5
class Samurai(Human):
	def __init__(self):
		super(Samurai, self).__init__()
		self.strength = 10
		print "...with a class Samurai"
	def sacrifice(self):
		self.health -= 5
		self.strength += 2
		return self

harry = Wizard()
rain = Ninja()
tom = Samurai()

print "Harry Health:",harry.health
print "Rain Health:",rain.health
print "Tom Health:",tom.health

harry.heal()
print "Harry Health:",harry.health

rain.steal()
print "Rain Stealth:",rain.stealth

tom.sacrifice()
print "Tom Health:",tom.health
print "Tom Strength:",tom.strength