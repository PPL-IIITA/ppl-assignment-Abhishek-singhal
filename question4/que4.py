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





gift(GiftObjectList,CoupleObjectList)
happiness(CoupleObjectList)



CoupleObjectList = sorted(CoupleObjectList,key=lambda x: x.happiness , reverse = False)

print("\n")
print("top 10 least happy couple : ")
for i in range(0,10):
	print(CoupleObjectList[i].boy.name +" and "+ CoupleObjectList[i].girl.name )

GirlObjectList2 = []

for girl in GirlObjectList:
	for i in range(0,10):
		if girl == CoupleObjectList[i].girl:
			girl.blacklist = CoupleObjectList[i].boy.name
			CoupleObjectList[i].boy.rstatus = "single"
			
			GirlObjectList2.append(girl)


for i in range(10):
	CoupleObjectList.remove(CoupleObjectList[0])

for gl in GirlObjectList2:
	for by in BoyObjectList:
		logs(gl.name+" is looking guy "+by.name)
		if  by.rstatus== "single" and gl.blacklist != by.name and by.is_eligible(gl.maintenance_budget,gl.attractiveness) and gl.is_eligible(by.budget):
			by.set_girlfriend = gl.name
			by.rstatus = "committed"
			gl.set_boyfriend = by.name
			gl.rstatus = "committed"
			print(gl.name+ " is in realtionship with "+by.name)
			logs(gl.name+ " is in realtionship with "+by.name)
			CoupleObjectList.append(Couple(by,gl))
			break


