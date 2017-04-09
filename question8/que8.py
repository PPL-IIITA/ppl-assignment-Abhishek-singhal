from utillitymaker import *
from library import gift2,happiness,logs,gift
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

print("Enter the type of gifting : ")
print("for gifting w.r.t to their budget enter 1 ")
print("for minimum gifting enter 2 (for defualt enter 0) ")

j = int(input())
if j==0 or j==1:
	gift(GiftObjectList,CoupleObjectList)
else:
	gift2(GiftObjectList,CoupleObjectList)
happiness(CoupleObjectList)

for cp in CoupleObjectList:
	print(cp.boy.name + " give gift to the " +cp.girl.name)
	for i in cp.gifts:
		print(i.name+" "+ i.type+" ")



