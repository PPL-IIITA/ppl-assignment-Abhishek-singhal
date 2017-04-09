from classes import Boy,Girl,Couple,Gift
import math,logging


def logs(log):
	logging.basicConfig(filename='logs.log',filemode='w',datefmt='%d/%m/%Y %I:%M:%S %p',format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',level=logging.DEBUG)
	logging.info(log)

def gift(GiftObjectList,CoupleObjectList):
	for cp in CoupleObjectList:
		if int(cp.boy.budget)< int(GiftObjectList[0].cost) and cp.boy.budget>=0:
			cp.boy.budget = int(GiftObjectList[0].cost)
			#print(cp.boy.budget)
		if cp.boy.type == "Miser" and cp.boy.budget>=0:
			miser(cp,GiftObjectList)
		elif cp.boy.type == "Generous" and cp.boy.budget>=0:
			generous(cp,GiftObjectList)
		elif cp.boy.budget>=0 and cp.boy.type == "Geek":
			geek(cp,GiftObjectList)

def miser(cp,GiftObjectList):
	giftbudget = int(cp.girl.maintenance_budget)
	if giftbudget <  int(GiftObjectList[0].cost):
		giftbudget = int(GiftObjectList[0].cost)
	for i in GiftObjectList:
		#print(type(i.cost))
		if giftbudget-int(i.cost)>=0:
			cp.gifts.append(i)
			logs(cp.boy.name+ " give a " +i.type+ " to the " +cp.girl.name)
			giftbudget-=int(i.cost)
 
def generous(cp,GiftObjectList):
	giftbudget = int(cp.boy.budget)
	for i in GiftObjectList:
		#print(int(i.cost))
		if giftbudget-int(i.cost)>=0:
			cp.gifts.append(i)
			logs(cp.boy.name+ " give a " +i.type+ " to the " +cp.girl.name)
			giftbudget-=int(i.cost)



def geek(cp,GiftObjectList):
	t=0
	x=0
	luxurycost=100	
	giftbudget = int(cp.girl.maintenance_budget)
	for i in GiftObjectList:
		#print(i.cost)
		if giftbudget-int(i.cost)>=0:
			cp.gifts.append(i)
			logs(cp.boy.name+ " give a " +i.type+ " to the " +cp.girl.name)
			giftbudget-=int(i.cost)
			t=t+1
		else:
			break

	for i  in range (t,len(GiftObjectList)):
		if GiftObjectList[i].type=="Luxury" and int(GiftObjectList[i].cost)< luxurycost:
			 luxurycost=int(GiftObjectList[i].cost)
			 x=i

	if (int(cp.boy.budget)-int(cp.girl.maintenance_budget) + giftbudget) >= luxurycost:
		cp.gifts.append(GiftObjectList[x])
		#logs(cp.boy.name+ " give a " +GiftObjectList[x].type+ " to the " +cp.girl.name)


def happiness(CoupleObjectList):
	for cp in CoupleObjectList:
		total=0
		for i in cp.gifts:
			total=total + int(i.cost)
		if cp.girl.type == "Choosy":
			cp.girl.happiness= math.log(total)
		elif cp.girl.type == "Normal":
			cp.girl.happiness = abs(total-int(cp.girl.maintenance_budget))
		else:
			cp.girl.happiness = math.exp((total-int(cp.girl.maintenance_budget)))
		if cp.boy.type == "Miser":
			cp.boy.happiness = int(cp.boy.budget)-int(cp.girl.maintenance_budget)
		elif cp.boy.type == "Generous":
			cp.boy.happiness = int(cp.girl.happiness) 
		else:
			cp.boy.happiness = int(cp.girl.intelligence)
		
		if(cp.boy.happiness<0):
			cp.boy.happiness = 0
		if cp.girl.happiness <0:
			cp.girl.happiness = 0
		cp.set_happiness()
		cp.set_compatibility()
