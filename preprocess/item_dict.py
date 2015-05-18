import csv
import os
import cPickle

f = open("../data/28_item.csv",'rb')
rows = csv.reader(f)
rows.next()
dictionary = {} #{(uid):[b1,b2,b3,b4,all,b/c,b/k]}
for row in rows:
	sample = row[0]  # Attention: tuple is hashable,but list is not hashable
	dictionary[sample] = [row[3],row[4],row[5],row[6],row[2], float(row[6])/int(row[2])]

a = []
for key in dictionary:
	a.append(dictionary[key][5])

a.sort()
#print a
print len(a)
print a[-1]

f = open("../data/dictionary/28_item_dict.pkl",'wb')
cPickle.dump(dictionary,f,-1)
f.close()
