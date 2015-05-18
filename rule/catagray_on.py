#-*-coding:utf-8-*-#
"""
提交12月18号加购物车且当天没买的,F1可达到7.6%

"""

import cPickle
import csv
import cPickle
#存储 (uid,iid)
from sys import path
path.append(r"../rule")
path.append(r"../howtoknow")
from caculateF1 import CaculateF1


item = cPickle.load(open("../data/dictionary/item.pkl","rb"))  #商品子集，19号购买商品所在集
user = cPickle.load(open("../data/dictionary/30_user_dict.pkl","rb"))
iitem = cPickle.load(open("../data/dictionary/30_item_dict.pkl","rb"))
user_item = cPickle.load(open("../data/dictionary/30_user_item_dict.pkl","rb"))
act_user = cPickle.load(open("../data/dictionary/30_act_user_dict.pkl","rb"))

day1 = cPickle.load(open("../data/dictionary/date/2014-12-17.pkl","rb"))
day1_c =  cPickle.load(open("../data/dictionary/date_u_c/2014-12-17.pkl","rb"))
day1_c_i =  cPickle.load(open("../data/dictionary/date_c_i/2014-12-17.pkl","rb"))
# day2 = cPickle.load(open("../data/dictionary/date/2014-12-15.pkl","rb"))
# day2_c =  cPickle.load(open("../data/dictionary/date_u_c/2014-12-15.pkl","rb"))
# day2 = cPickle.load(open("../data/dictionary/date/2014-12-16.pkl","rb"))
# day3 = cPickle.load(open("../data/dictionary/date/2014-12-15.pkl","rb"))

h23 = cPickle.load(open("../data/dictionary/17/23.pkl","rb"))
h22 = cPickle.load(open("../data/dictionary/17/22.pkl","rb"))

def model_one():
	
	result = {}
	user_r = {}

	for key in day1:
		uid,iid = key
		cid = day1[key][2][0]
		ckey = (uid, cid)
		#对于商品子集里的商品，18号加购物车且没买的，生成提交文件
		if  item.has_key(iid) and day1[key][0][2]>0 and day1[key][0][3]==0 and day1[key][0][0] > 1 and day1[key][0][0] < 11:
	            	# if day1_c[ckey][0][3] == 0:
	            	if day1_c[ckey][0][0] >2 and day1_c[ckey][0][0] < 40 and day1_c[ckey][0][3] == 0:
	           			#if item_rat[iid][5] > 0.02 and item_div_user > 0.002:
		           	if act_user[uid] < 95:# and int(iitem[iid][3]) < 7:
		           		if float(user_item[key])/float(user[uid][4]) > 0.001:###################################
		           					if user_r.has_key(uid):
		           						print user_item[key]
		           					else:
		           						user_r[uid] = 1
								result[key] = 1
						# if day1_c[ckey][0][2] < 3:
						# 	result[key] = 1
						# else:
						# 	minn = 0
						# 	for ikey in day1_c_i:
						# 		ccid, iiid = ikey
						# 		if ccid == cid:
						# 			if minn == 0:
						# 				minn = iiid
						# 			if day1_c_i[ikey][0][2] < day1_c_i[(ccid, minn)][0][2]:
						# 				result[(uid, minn)] = 1
						# 				minn = iiid
						# 			else:
						# 				result[(uid,iiid)] = 1	


	for key in h23:
    		uid,iid = key
    		ckey = (uid, day1[key][2][0])
    		#对于商品子集里的商品，18号加购物车且没买的，生成提交文件
    		if  item.has_key(iid) and h23[key][0][2]>0 and h23[key][0][3]==0 and day1_c[ckey][0][3] == 0:
		        #if day1_c[ckey][0][0] > 90:
		        # rows = csv.reader(open("../data/user/"+key[0]+".csv","rb"))
		        # rows.next()           
		        # for row in rows:
		        #     if row[0] == "2014-12-18" and row[1] == key[1] and row[2] == "3":
		               result[key] = 1

	# for key in h22:
 #    		uid,iid = key
 #    		ckey = (uid, day1[key][2][0])
 #    		#对于商品子集里的商品，18号加购物车且没买的，生成提交文件
 #    		if  item.has_key(iid) and h22[key][0][2]>0 and h22[key][0][3]==0 and day1_c[ckey][0][3] == 0:
	# 	        # rows = csv.reader(open("../data/user/"+key[0]+".csv","rb"))
	# 	        # rows.next()           
	# 	        # for row in rows:
	# 	        #     if row[0] == "2014-12-18" and row[1] == key[1] and row[2] == "3":
	# 	               result[key] = 1


	# for key in day2:
	#     uid,iid = key
	#     ckey = (uid, day2[key][2][0])
	#     #对于商品子集里的商品，18号加购物车且没买的，生成提交文件
	#     if  item.has_key(iid) and day2[key][0][2]>0 and day2[key][0][3]==0: #or day2[key][0][1] > 0 and day2[key][0][0] > 8:
	#             # if day2_c[ckey][0][3] == 0:
	#             if day2_c[ckey][0][0] >5 and day2_c[ckey][0][0] < 40 and day2_c[ckey][0][3] == 0:
	#             	if day1_c.has_key(ckey) and day1_c[ckey][0][3] > 0:
	#             		continue
	#             	result[key] = 1


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

model_one()
CaculateF1("../result/user_item_buy_18.csv", "../result/liyp_click_not_buy_predict_17.csv")

# a = []
# for key in user_item:
# 	uid, iid = key
# 	usr_div_item = float(user_item[key])/float(user[uid][4])
# 	a.append(usr_div_item)
# a.sort()
# print len(a)
# print a[len(a)/2]