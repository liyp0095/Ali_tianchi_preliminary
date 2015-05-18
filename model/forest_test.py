#-*-coding:utf-8-*-#

import cPickle
import csv
from sklearn.ensemble import RandomForestClassifier

item = cPickle.load(open("../data/dictionary/item.pkl","rb"))  #商品子集，19号购买商品所在集
day2 = cPickle.load(open("../data/dictionary/date/2014-12-17.pkl","rb"))
day1 = cPickle.load(open("../data/dictionary/date/2014-12-16.pkl","rb"))
# day3 = cPickle.load(open("../data/dictionary/date/2014-12-15.pkl","rb"))

X = []
Y = []
    

for key in day1:
    uid,iid = key
    one_note_1 = [day1[key][0][0], day1[key][0][1], day1[key][0][2], day1[key][0][3]]
    X.append(one_note_1)
    if day2.has_key(key) and day2[key][0][3] > 0:
    	Y.append(1)
    else:
    	Y.append(0)

# X = [[0,0],[1,1],[0,1]]
# Y = [0,1,1]
clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X,Y)

filein = []

for key in day2:
	one_note_2 = [day2[key][0][0], day2[key][0][1], day2[key][0][2], day2[key][0][3]]
    	print clf.predict(one_note_2)
    #对于商品子集里的商品，18号加购物车且没买的，生成提交文件
    # if  item.has_key(iid) and day1[key][0][2]>0 and day1[key][0][3]==0: #or day1[key][0][1] > 0 and day1[key][0][0] > 8:
    #         user_buy_cat = uid_cat_num(uid,day1[key][2][0])
    #         if user_buy_cat > 5 and user_buy_cat < 50:
    #             result[key] = 1

# result = clf.predict(filein)

for key in result:
	print key




