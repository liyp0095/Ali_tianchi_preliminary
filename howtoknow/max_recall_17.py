import os
import csv
import cPickle

day1 = cPickle.load(open("../data/dictionary/date/2014-12-17.pkl","rb"))

file1 = open("../result/user_item_buy_18.csv")
std_result = csv.reader(file1)
std_result.next()
dictionary = {}
res_count = 0
for row in std_result:
 	res_count += 1
	uid = row[0]
	iid = row[1]
	key = (uid, iid)
	dictionary[key] = 1

count = 0
for key in day1:
	if dictionary.has_key(key) and day1[key][0][2] > 0 and day1[key][0][3] == 0:
		print key
		count += 1

print "generate submission file,total %d  (uid,iid)" %count