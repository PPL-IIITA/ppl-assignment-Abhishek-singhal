class person:
	def __init__(self,name,attractiveness,intelligence,typeof):
		self.name = name
		self.attractiveness = attractiveness
		self.intelligence = intelligence
		self.type = typeof

class Boy(person):
	def __init__(self,name,attractiveness,intelligence,budget,min_girlAttraction,typeof):
		person.__init__(self,name,attractiveness,intelligence,typeof)
		self.budget=budget
		self.min_girlAttraction=min_girlAttraction
		self.rstatus = "single"
		self.happiness = 0
		self.girlfriend = ''
	
	def modify_budget(self,budget):
		self.budget=budget
			
	def is_eligible(self, maintenance_budget, attractiveness):
		if (self.budget >= maintenance_budget) and (attractiveness >= self.min_girlAttraction):
			return True
		else:
			return False

class Girl(person):
	def __init__(self,name,attractiveness,maintenance_budget,intelligence,typeof):
		person.__init__(self,name,attractiveness,intelligence,typeof)
		self.maintenance_budget=maintenance_budget
		self.rstatus = "single"
		self.happiness = 0
		self.boyfriend = ''
		self.blacklist = 'none'
			
	def is_eligible(self, budget):
		if (self.maintenance_budget <= budget):
			return True
		else:
			return False

class Gift :
	def __init__(self,name,cost,value,typeof):
		self.name = name
		self.cost = cost
		self.value = value
		self.type = typeof

class Couple:
	def __init__(self, boy, girl):
		self.girl = girl
		self.boy = boy
		self.gifts = []
		self.compatibility = 0
		self.happiness = 0
			
	def set_compatibility(self):
		a = int(self.boy.budget) - int(self.girl.maintenance_budget)
		b = abs(int(self.boy.attractiveness) - int(self.girl.attractiveness))
		c = abs(int(self.boy.intelligence) - int(self.girl.intelligence))
		self.compatibility = a+b+c

	def set_happiness(self):
		self.happiness = int(self.boy.happiness) + int(self.girl.happiness)
