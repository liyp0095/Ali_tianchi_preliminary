#-*-coding:utf-8-*-#
"""
get buy note one day
"""

import cPickle
import csv


#存储 (uid,iid)
result = {}


item = cPickle.load(open("../data/dictionary/item.pkl","rb"))  #商品子集，19号购买商品所在集
day = cPickle.load(open("../data/dictionary/date/2014-11-28.pkl","rb"))

for key in day:
    uid,iid = key
    #对于商品子集里的商品，18号加购物车且没买的，生成提交文件
    if item.has_key(iid) and day[key][0][3]>0:
        # rows = csv.reader(open("../data/user/"+key[0]+".csv","rb"))
        # rows.next()           
        # for row in rows:
        #     if row[0] == "2014-12-18" and row[1] == key[1] and row[2] == "3":
               result[key] = 1



#写入文件
f = open("../result/user_item_buy_11_28.csv","wb")
write = csv.writer(f)
write.writerow(["user_id","item_id"])
total = 0
for key in result:
    write.writerow(key)
    total += 1 
print "generate submission file,total %d  (uid,iid)" %total
f.close()
