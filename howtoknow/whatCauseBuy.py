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

	# for key in dictionary:
	# 	dayone = [day2[key][0][0], day2[key][0][1], day2[key][0][2], day2[key][0][3]]
	# 	if day3.has_key(key):
	# 		daytwo = [day3[key][0][0], day3[key][0][1], day3[key][0][2], day3[key][0][3]]
	# 	else:
	# 		daytwo = [0,0,0,0]
	# 	if day4.has_key(key):
	# 		daythree = [day4[key][0][0], day4[key][0][1], day4[key][0][2], day4[key][0][3]]
	# 	else:
	# 		daythree = [0,0,0,0]
	# 	if day5.has_key(key):
	# 		dayfour = [day5[key][0][0], day5[key][0][1], day5[key][0][2], day5[key][0][3]]
	# 	else:
	# 		dayfour = [0,0,0,0]
	# 	if day6.has_key(key):
	# 		dayfive = [day6[key][0][0], day6[key][0][1], day6[key][0][2], day6[key][0][3]]
	# 	else:
	# 		dayfive = [0,0,0,0]
	# 	if day7.has_key(key):
	# 		daysix = [day7[key][0][0], day7[key][0][1], day7[key][0][2], day7[key][0][3]]
	# 	else:
	# 		daysix = [0,0,0,0]
	# 	print dayone,"\t",daytwo,"\t",daythree,"\t", dayfour,"\t",dayfive,"\t",daysix
	for key in dictionary:
		day_in_hour = []
		for i in range(0, 24):
			print day2[key][3][int(i)]
		print day_in_hour


day1 = cPickle.load(open("../data/dictionary/date/2014-12-18.pkl","rb"))
day2 = cPickle.load(open("../data/dictionary/date/2014-12-17.pkl","rb"))
day3 = cPickle.load(open("../data/dictionary/date/2014-12-16.pkl","rb"))
day4 = cPickle.load(open("../data/dictionary/date/2014-12-15.pkl","rb"))
day5 = cPickle.load(open("../data/dictionary/date/2014-12-14.pkl","rb"))
day6 = cPickle.load(open("../data/dictionary/date/2014-12-13.pkl","rb"))
day7 = cPickle.load(open("../data/dictionary/date/2014-12-12.pkl","rb"))

xianshi()