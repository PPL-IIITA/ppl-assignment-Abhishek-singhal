from utillitymaker import *
from classes import Boy,Girl,Couple,Gift
import csv, logging,math
from library import logs,gift,happiness
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


for i in giftlist:
	GiftObjectList.append(Gift(i[0],i[1],i[2],i[3]))
GiftObjectList = sorted(GiftObjectList,key=lambda x: x.cost)


for i in boylist:
	BoyObjectList.append(Boy(i[0],i[1],i[2],i[3],i[4],i[5]))


for i in girllist:
	GirlObjectList.append(Girl(i[0],i[1],i[2],i[3],i[4]))

i=0
j=0
GirlObjectList2 = sorted(GirlObjectList,key=lambda x: x.attractiveness ,reverse = True)	
while i<20:
	gl = GirlObjectList[i]
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
	i=i+1
	by = BoyObjectList[j]
	for gl in GirlObjectList2:
		logs(by.name+" is looking guy "+gl.name)
		if by.rstatus == gl.rstatus and by.rstatus== "single" and by.is_eligible(gl.maintenance_budget,gl.attractiveness) and gl.is_eligible(by.budget):
			by.set_girlfriend = gl.name
			by.rstatus = "committed"
			gl.set_boyfriend = by.name
			gl.rstatus = "committed"
			print(gl.name+ " is in realtionship with "+by.name)
			logs(gl.name+ " is in realtionship with "+by.name)
			CoupleObjectList.append(Couple(by,gl))
			break
	j=j+1





gift(GiftObjectList,CoupleObjectList)
happiness(CoupleObjectList)

		
		#print(cp.compatibility
CoupleObjectList = sorted(CoupleObjectList,key=lambda x: x.happiness , reverse = True)
print("top 10 most happy couple\n")
for i in range(0,10):
	print(CoupleObjectList[i].boy.name +" and "+ CoupleObjectList[i].girl.name )





