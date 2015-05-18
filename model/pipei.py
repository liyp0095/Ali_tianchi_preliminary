import os
import csv
import cPickle

def xiangguan(a, b):
	if len(a) == len(b):
		a_victor_lenth = 0
		for i in a:
			a_victor_lenth += i*i
		a_victor_lenth = a_victor_lenth ** 0.5

		b_victor_lenth = 0
		for i in b:
			b_victor_lenth += i*i
		b_victor_lenth = b_victor_lenth ** 0.5

		xishu = 0
		for i in range(0, len(a)):
			xishu += float(a[i])*b[i]/a_victor_lenth/b_victor_lenth
		return xishu
	else:
		return 0

# day5 = cPickle.load(open("../data/dictionary/date/2014-12-14.pkl","rb"))
# day6 = cPickle.load(open("../data/dictionary/date/2014-12-13.pkl","rb"))
# day7 = cPickle.load(open("../data/dictionary/date/2014-12-12.pkl","rb"))
# day8 = cPickle.load(open("../data/dictionary/date/2014-12-11.pkl","rb"))
# day9 = cPickle.load(open("../data/dictionary/date/2014-12-10.pkl","rb"))
# day10 = cPickle.load(open("../data/dictionary/date/2014-12-9.pkl","rb"))
# day11 = cPickle.load(open("../data/dictionary/date/2014-12-8.pkl","rb"))
# day12 = cPickle.load(open("../data/dictionary/date/2014-12-7.pkl","rb"))

def pipei():
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
		click = day2[key][0][0]
		store = day2[key][0][1]
		cart = day2[key][0][2]
		buy = day2[key][0][3]
		dayone = [click, store, cart, buy]

		if day3.has_key(key):
		    	click1 = day3[key][0][0]
			store1 = day3[key][0][1]
			cart1 = day3[key][0][2]
			buy1 = day3[key][0][3]
			daytwo = [click1, store1, cart1, buy1]
    			print xiangguan(dayone, daytwo),"    ", dayone, daytwo


day1 = cPickle.load(open("../data/dictionary/date/2014-12-18.pkl","rb"))
day2 = cPickle.load(open("../data/dictionary/date/2014-12-17.pkl","rb"))
day3 = cPickle.load(open("../data/dictionary/date/2014-12-16.pkl","rb"))
day4 = cPickle.load(open("../data/dictionary/date/2014-12-15.pkl","rb"))

pipei()
# a = [1,2,3,4]
# b = [5,6,7,8]
# print a,b
# print xiangguan(a, b)


