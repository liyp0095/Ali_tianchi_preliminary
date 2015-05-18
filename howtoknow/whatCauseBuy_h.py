import os
import csv
import cPickle

def xianshi():
	file = open("../result/user_item_buy_17.csv")
	res = csv.reader(file)
	res.next()
	dictionary = {}
	for row in res:
		uuid = row[0]
		iiid = row[1]
		key1 = (uuid, iiid)
		dictionary[key1] = 1

	for key in dictionary:
		for i in range(0, 24):
			if day2[key][int(i)][0] != 0 or day2[key][int(i)][1] != 0 or day2[key][int(i)][2] != 0 or day2[key][int(i)][3] != 0:
				print day2[key][int(i)],i,'\t',
		print ' '

day1 = cPickle.load(open("../data/dictionary/date_hour/2014-12-18.pkl","rb"))
day2 = cPickle.load(open("../data/dictionary/date_hour/2014-12-17.pkl","rb"))
day3 = cPickle.load(open("../data/dictionary/date_hour/2014-12-16.pkl","rb"))

xianshi()