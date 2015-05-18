import csv
import os
import cPickle

f = open("../data/28_user_item.csv",'rb')
rows = csv.reader(f)
rows.next()
dictionary = {} #{(uid):[b1,b2,b3,b4,all,b/c,b/k]}
for row in rows:
	sample = (row[0],row[1])  # Attention: tuple is hashable,but list is not hashable
	dictionary[sample] = row[3]

f = open("../data/dictionary/28_user_item_dict.pkl",'wb')
cPickle.dump(dictionary,f,-1)
f.close()
