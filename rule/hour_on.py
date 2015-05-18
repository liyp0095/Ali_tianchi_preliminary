#-*-coding:utf-8-*-#
"""
提交12月18号加购物车且当天没买的,F1可达到7.6%

"""

import cPickle
import csv


#存储 (uid,iid)
result = {}


item = cPickle.load(open("../data/dictionary/item.pkl","rb"))  #商品子集，19号购买商品所在集
day = cPickle.load(open("../data/dictionary/date/2014-12-17.pkl","rb"))
day_c =  cPickle.load(open("../data/dictionary/date_u_c/2014-12-17.pkl","rb"))
h23 = cPickle.load(open("../data/dictionary/17/23.pkl","rb"))
h22 = cPickle.load(open("../data/dictionary/17/22.pkl","rb"))

for key in h23:
    uid,iid = key
    ckey = (uid, day[key][2][0])
    #对于商品子集里的商品，18号加购物车且没买的，生成提交文件
    if  item.has_key(iid) and h23[key][0][1]>0 and h23[key][0][3]==0 and day_c[ckey][0][3] == 0:
        #if day_c[ckey][0][0] > 90:
        # rows = csv.reader(open("../data/user/"+key[0]+".csv","rb"))
        # rows.next()           
        # for row in rows:
        #     if row[0] == "2014-12-18" and row[1] == key[1] and row[2] == "3":
               result[key] = 1

# for key in h22:
#     uid,iid = key
#     ckey = (uid, day[key][2][0])
#     #对于商品子集里的商品，18号加购物车且没买的，生成提交文件
#     if  item.has_key(iid) and h22[key][0][2]>0 and h22[key][0][3]==0 and day_c[ckey][0][3] == 0:
#         # rows = csv.reader(open("../data/user/"+key[0]+".csv","rb"))
#         # rows.next()           
#         # for row in rows:
#         #     if row[0] == "2014-12-18" and row[1] == key[1] and row[2] == "3":
#         if day_c[ckey][0][0] > 90:
#                result[key] = 1

# for key in day:
#     uid,iid = key
#     ckey = (uid, day[key][2][0])
#     #对于商品子集里的商品，18号加购物车且没买的，生成提交文件
#     if  item.has_key(iid) and day[key][0][2]>0 and day[key][0][3]==0: #or day[key][0][1] > 0 and day[key][0][0] > 8:
#             # if day_c[ckey][0][3] == 0:
#             if day_c[ckey][0][0] >2 and day_c[ckey][0][0] < 30 and day_c[ckey][0][3] == 0:

#                 result[key] = 1


#写入文件
f = open("../result/liyp_click_not_buy_predict_17.csv","wb")
write = csv.writer(f)
write.writerow(["user_id","item_id"])
total = 0
for key in result:
    write.writerow(key)
    total += 1 
print "generate submission file,total %d  (uid,iid)" %total
f.close()
