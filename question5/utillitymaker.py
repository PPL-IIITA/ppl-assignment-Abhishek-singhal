import random
import csv
from operator import itemgetter


def boy_util():
	Boys = []
	BoyType = ["Miser","Generous","Geek"]
	for x in range(1,201):
		Boys.append(("Boy"+str(x),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),BoyType[random.randint(0,2)]))
	Boys = sorted(Boys, key=itemgetter(1))
	
	with open('boylist.csv', 'w') as csv_file:
		 writer = csv.writer(csv_file,delimiter = ',')  
		 for i in Boys:
		 	writer.writerow(i)


def girl_util():
	Girls = []
	GirlType = ["Choosy","Normal","Desperate"]
	for x in range(1,21):
		Girls.append(("Girl"+str(x),random.randint(0,100),random.randint(0,100),random.randint(0,100),GirlType[random.randint(0,2)]))
	Girls = sorted(Girls, key=itemgetter(2))
	
	with open('girllist.csv', 'w') as csv_file:
		 writer = csv.writer(csv_file,delimiter = ',')  
		 for i in Girls:
		 	writer.writerow(i)


def gift_util():
	Gifts = []
	GiftType = ["Essential","Luxury","utility"]
	for x in range(1,21):
		Gifts.append(("Gift"+str(x),random.randint(0,100),random.randint(0,100),GiftType[random.randint(0,2)]))

	with open('giftlist.csv', 'w') as csv_file:
		 writer = csv.writer(csv_file,delimiter = ',')  
		 for i in Gifts:
		 	writer.writerow(i)
