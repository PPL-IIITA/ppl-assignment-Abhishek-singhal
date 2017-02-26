class Boy:
	def __init__(self,name,attrectivness,intelligence,budget,min_girlAttraction,typeof):
		self.name=name
		self.attrectivness=attrectivness
		self.intelligence=intelligence
		self.budget=budget
		self.min_girlAttraction=min_girlAttraction
		self.type=typeof
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

class Girl:
	def __init__(self,name,attractiveness,maintenance_budget,intelligence,typeof):
		self.name=name
		self.attractiveness=attractiveness
		self.intelligence=intelligence
		self.maintenance_budget=maintenance_budget
		self.type=typeof
		self.rstatus = "single"
		self.happiness = 0
		self.boyfriend = ''
	
	def modify_maintenance_budget(self,budget):
		self.budget=budget
			
	def is_eligible(self, budget):
		if (self.maintenance_budget <= budget):
			return True
		else:
			return False