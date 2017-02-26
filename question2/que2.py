from utillitymaker import *
from classes import Boy,Girl,Couple,Gift
import csv, logging,math
#from giftprocedure import *

girl_util()
boy_util()
gift_util()

with open('boylist.csv', 'r') as f:
    reader = csv.reader(f)
    boylist = list(reader)

with open('girllist.csv', 'r') as f:
    reader = csv.reader(f)
    girllist = list(reader)

with open('giftlist.csv', 'r') as f:
    reader = csv.reader(f)
    giftlist = list(reader)

BoyObjectList = []
GirlObjectList = []
CoupleObjectList = []
GiftObjectList = []


def logs(log):
	logging.basicConfig(filename='logs.log',filemode='w',datefmt='%d/%m/%Y %I:%M:%S %p',format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',level=logging.DEBUG)
	logging.info(log)
for i in giftlist:
	GiftObjectList.append(Gift(i[0],i[1],i[2],i[3]))

GiftObjectList = sorted(GiftObjectList,key=lambda x: x.cost)

for i in boylist:
	BoyObjectList.append(Boy(i[0],i[1],i[2],i[3],i[4],i[5]))

for i in girllist:
	GirlObjectList.append(Girl(i[0],i[1],i[2],i[3],i[4]))

for gl in GirlObjectList:
	for by in BoyObjectList:
		logs(gl.name+" is looking guy "+by.name)
		if by.rstatus == gl.rstatus and by.rstatus== "single" and by.is_eligible(gl.maintenance_budget,gl.attractiveness) and gl.is_eligible(by.budget):
			by.set_girlfriend = gl.name
			by.rstatus = "committed"
			gl.set_boyfriend = by.name
			gl.rstatus = "committed"
			print(gl.name+ " is in realtionship with "+by.name)
			logs(gl.name+ " is in realtionship with "+by.name)
			CoupleObjectList.append(Couple(by,gl))
			break

def gift():
	for cp in CoupleObjectList:
		if int(cp.boy.budget)< int(GiftObjectList[0].cost):
			cp.boy.budget = int(GiftObjectList[0].cost)
			#print(cp.boy.budget)
		if cp.boy.type == "Miser":
			miser(cp)
		elif cp.boy.type == "Generous":
			generous(cp)
		else:
			geek(cp)

def miser(cp):
	giftbudget = int(cp.girl.maintenance_budget)
	if giftbudget <  int(GiftObjectList[0].cost):
		giftbudget = int(GiftObjectList[0].cost)
	for i in GiftObjectList:
		#print(type(i.cost))
		if giftbudget-int(i.cost)>=0:
			cp.gifts.append(i)
			logs(cp.boy.name+ " give a " +i.type+ " to the " +cp.girl.name)
			giftbudget-=int(i.cost)
 
def generous(cp):
	giftbudget = int(cp.boy.budget)
	for i in GiftObjectList:
		#print(int(i.cost))
		if giftbudget-int(i.cost)>=0:
			cp.gifts.append(i)
			logs(cp.boy.name+ " give a " +i.type+ " to the " +cp.girl.name)
			giftbudget-=int(i.cost)



def geek(cp):
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
		logs(cp.boy.name+ " give a " +GiftObjectList[x].type+ " to the " +cp.girl.name)


gift()
for cp in CoupleObjectList:
	print(cp.boy.name + " give gift to the " +cp.girl.name)
	for i in cp.gifts:
		print(i.name+" "+ i.type+" ")


def happiness():
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
		
		print(cp.compatibility)

happiness()
CoupleObjectList = sorted(CoupleObjectList,key=lambda x: x.happiness , reverse = True)
print("top 10 most happy couple\n")
for i in range(0,10):
	print(CoupleObjectList[i].boy.name +" and "+ CoupleObjectList[i].girl.name )
	#print(CoupleObjectList[i].happiness)
print("top 10 best couple\n")

CoupleObjectList = sorted(CoupleObjectList,key=lambda x: x.compatibility,reverse =True)
for i in range(0,10):
 	print(CoupleObjectList[i].boy.name +" and "+ CoupleObjectList[i].girl.name )



