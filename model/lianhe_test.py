#-*-coding:utf-8-*-#
"""
提交12月18号加购物车且当天没买的,F1可达到7.6%

"""

import cPickle
import csv


def uid_cat_num(user_id, catagray):
    count = 0
    for key in day1:
        uuid, iiid = key
        if day1[key][2][0] == catagray and uuid == user_id and day1[key][0][0] > 0:
            count += day1[key][0][0]
    return count

#存储 (uid,iid)
result = {}

item = cPickle.load(open("../data/dictionary/item.pkl","rb"))  #商品子集，19号购买商品所在集
day1 = cPickle.load(open("../data/dictionary/date/2014-12-17.pkl","rb"))
day2 = cPickle.load(open("../data/dictionary/date/2014-12-16.pkl","rb"))
day3 = cPickle.load(open("../data/dictionary/date/2014-12-15.pkl","rb"))

#####################################################
X = []
Y = []
for key in day2:
    uid,iid = key
    if day2[key][0][3] > 0:
        one_note_1 = [uid_cat_num(uid,day2[key][2][0]), day2[key][0][0], day2[key][0][1], day2[key][0][2], day2[key][0][3]]
        X.append(one_note_1)
        if day1.has_key(key) and day1[key][0][3] > 0:
            Y.append(1)
        else:
            Y.append(0)

# X = [[0,0],[1,1],[0,1]]
# Y = [0,1,1]
clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X,Y)
#############################################################

my_in = []
for key in day1:
    uid,iid = key
    #对于商品子集里的商品，18号加购物车且没买的，生成提交文件
    if  item.has_key(iid) and day1[key][0][2]>0 and day1[key][0][3]==0: #or day1[key][0][1] > 0 and day1[key][0][0] > 8:
            user_buy_cat = uid_cat_num(uid,day1[key][2][0])
            if user_buy_cat > 2 and user_buy_cat < 30:
                note = [user_buy_cat, day1[key][0][0], day1[key][0][1], day1[key][0][2], day1[key][0][3]]
                a = clf.predict(note)
                if a[0]==1:
                    result[key] = 1

# my_res = clf.predict(my_in)

# for key in day2:
#     uid,iid = key
#     #对于商品子集里的商品，17号加购物车且17，18没买的，生成提交文件
#     if  item.has_key(iid) and day2[key][0][2]>0 and day2[key][0][3]==0 and day2[key][0][0] > 5: #iid在商品子集中，当天加入购物车，且没有购买
#                 if day1.has_key(key) and day1[key][0][3] > 0:
#                         continue
#                 result[key] = 1

# for key in day2:
#     uid,iid = key
#     #对于商品子集里的商品，17号加购物车且17，18没买的，生成提交文件
#     if  item.has_key(iid) and day2[key][0][2]>0 and day2[key][0][3]==0 and day2[key][0][0] > 0: #iid在商品子集中，当天加入购物车，且没有购买
#                 if day1.has_key(key) and day1[key][0][0] > 0 and day1[key][0][3] == 0:
#                         result[key] = 1


# for key in day3:
#     uid,iid = key
#     #对于商品子集里的商品，17号加购物车且17，18没买的，生成提交文件
#     if  item.has_key(iid) and day3[key][0][2]>0 and day3[key][0][3]==0 and day3[key][0][0] > 7: #iid在商品子集中，当天加入购物车，且没有购买
#                 if day1.has_key(key) and day1[key][0][3] > 0:
#                         continue
#                 if day2.has_key(key) and day2[key][0][3] > 0:
#                         continue
#                 result[key] = 1

# for key in day1:
#     uid,iid = key
#     #对于商品子集里的商品，18号加购物车且没买的，生成提交文件
#     if  item.has_key(iid) and day1[key][0][3]>0: #or day1[key][0][1] > 0 and day1[key][0][0] > 8:
#                if day2.has_key(key) and day2[key][0][3] > 0:
#                             result[key] = 1



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

