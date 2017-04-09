class Boy:
	def __init__(self,name,attractiveness,intelligence,budget,min_girlAttraction,typeof):
		self.name=name
		self.attractiveness=attractiveness
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

class sort:
	def __init__(self,boy,couple):
		self.boy = boy
		self.couple = couple
	def sorting(self):
		for by in self.boy:
			for cp in self.couple:
				if by.name == cp.boy.name:
					print(by.name + " is committed with "+cp.girl.name)


class BinarySort(sort):
	def __init__(self,boy,couple):
		sort.__init__(self,boy,couple)
	def sorting(self):
		for by in self.boy:
			first = 0
			last = len(self.couple)-1
			found = False
			while first<=last and not found:
				 midpoint = (first + last)/2
				 if self.couple[midpoint].happiness == int(by.happiness) + int(self.couple[midpoint].girl.happiness) and by.rstatus != "single":
				 	print(by.name + " is committed with "+self.couple[midpoint].girl.name)
				 	found = True
				 else:
				 	if int(by.happiness) +int(self.couple[midpoint].girl.happiness) < self.couple[midpoint].happiness:
				 		last = midpoint-1
				 	else:
				 		first = midpoint+1

class hashing(sort):
	def __init__(self,boy,couple):
		sort.__init__(self,boy,couple)
	def sorting(self):
		coupledict = {}
		for by in self.boy:
			coupledict[by.name] = ''
		for cp in self.couple:
			coupledict[cp.boy.name] = cp.girl.name
		for by in self.boy:
			if coupledict[by.name] != '':
				print (by.name + " is committed with "+coupledict[by.name])
