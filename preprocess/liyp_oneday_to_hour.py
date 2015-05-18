#-*- coding:utf8 -*-#
"""
---------------------------------------
*功能：遍历/data/date里的文件，然后读取并提样本和特征。如"2014-12-18.csv"，文件里面出现的所有用户，以及用户有过行为的商品，都会分别生成样本(uid,iid)。
*举例：用户u1点击过i1、i2两件商品，买过i3这件商品，则该用户可以构建三个样本：(u1,i1)、（u1，i2）、（u1，i3）。
*样本-特征：样本名(uid,iid)以元组格式作为字典key，样本的特征向量以list格式[feat1,feat2...] 作为字典value。PS：字典的查找会快一点，以空间换时间。
*保存：生成的 样本-特征 保存为 "文件名.pkl" 文件，利用cPickle保存。
---------------------------------------

"""

import os
import csv
import cPickle

def genUidIid():	
	os.mkdir("../data/dictionary/15")
	direction = "../data/date/"
	file_list = os.listdir(direction)
	file_name = "2014-12-15.csv"
	for i in range(0,24):
	    file_path = direction+file_name
	    f = open(file_path,'rb')
	    rows = csv.reader(f)
	    rows.next()
	    dictionary = {} #{(uid,iid):[[b1,b2,b3,b4],[g1,g2..],[c1,c2..],[h1,h2..]]}
	    for row in rows:
	    	if i == int(row[5]):
			sample = (row[0],row[1])  # Attention: tuple is hashable,but list is not hashable
			if dictionary.has_key(sample):
			    dictionary[sample][0][int(row[2])-1] += 1
			else:
			    dictionary[sample]=[[0,0,0,0]]
			    dictionary[sample][0][int(row[2])-1] = 1
#		dictionary[sample][3].sort()
	    f.close()
            
	    f = open("../data/dictionary/15/"+str(i)+".pkl",'wb')
	    cPickle.dump(dictionary,f,-1)
	    f.close()

genUidIid()