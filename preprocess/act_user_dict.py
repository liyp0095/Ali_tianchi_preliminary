import csv
import os
import cPickle

f = open("../data/28_act_user.csv",'rb')
rows = csv.reader(f)
rows.next()
dictionary = {} #{(uid):[b1,b2,b3,b4,all,b/c,b/k]}
for row in rows:
	sample = row[0]  # Attention: tuple is hashable,but list is not hashable
	if dictionary.has_key(sample):
		if int(row[3]) > 20:
			dictionary[sample] += 1
	else:
		dictionary[sample] = 0 

a = []
for key in dictionary:
	a.append(dictionary[key])
#	print key, dictionary[key]
a.sort()
print a
print len(a)
print a[len(a)*7/8]

f = open("../data/dictionary/28_act_user_dict.pkl",'wb')
cPickle.dump(dictionary,f,-1)
f.close()
