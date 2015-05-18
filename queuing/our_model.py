#-*-coding:utf-8-*-#
''''''

import cPickle
import csv
import cPickle

from sys import path
path.append(r"../howtoknow")
from caculateF1 import CaculateF1

#

#sub item
item = cPickle.load(open("../data/dictionary/item.pkl","rb"))  #商品子集，19号购买商品所在集
#data of 30 days
user = cPickle.load(open("../data/dictionary/user_dict.pkl","rb"))
iitem = cPickle.load(open("../data/dictionary/item_dict.pkl","rb"))
user_item = cPickle.load(open("../data/dictionary/user_item_dict.pkl","rb"))
act_user = cPickle.load(open("../data/dictionary/act_user_dict.pkl","rb"))
#data of yesterday
day1 = cPickle.load(open("../data/dictionary/date/2014-12-17.pkl","rb"))
day1_c =  cPickle.load(open("../data/dictionary/date_u_c/2014-12-17.pkl","rb"))
day1_c_i =  cPickle.load(open("../data/dictionary/date_c_i/2014-12-17.pkl","rb"))
# day2 = cPickle.load(open("../data/dictionary/date/2014-12-15.pkl","rb"))
# day2_c =  cPickle.load(open("../data/dictionary/date_u_c/2014-12-15.pkl","rb"))
# day2 = cPickle.load(open("../data/dictionary/date/2014-12-16.pkl","rb"))
# day3 = cPickle.load(open("../data/dictionary/date/2014-12-15.pkl","rb"))
#data of yesterday in hour
h23 = cPickle.load(open("../data/dictionary/17/23.pkl","rb"))
h22 = cPickle.load(open("../data/dictionary/17/22.pkl","rb"))

def model_one(enable_today_cart, 	today_cart, 
		enable_today_buy, 	today_buy,
		enable_today_click, 	today_click_up, today_click_down,
		enable_today_cat_click, 	today_cat_click_up, today_cat_click_down,
		enable_today_cat_buy, 	today_cat_buy,
		enable_act_hour, 	act_hour,
		enable_item, 		item_0, item_1, item_2, item_3,
		enable_item_user_rate, 	item_user_rate,
		enable_item_buy_rate, 	item_buy_rate
		):
	result = {}
	item_r = {}

	for key in day1:
		uid,iid = key
		cid = day1[key][2][0]
		ckey = (uid, cid)

		if item.has_key(iid):
			if (day1[key][0][2]>today_cart and day1[key][0][3]==today_buy) or enable_today_buy:
				if (day1_c[ckey][0][0] >today_cat_click_up and day1_c[ckey][0][0] < today_cat_click_down) or enable_today_cat_click:
					if day1_c[ckey][0][3] == today_cat_buy  or enable_today_cat_buy:
						if (day1[key][0][0] > today_click_up and day1[key][0][0] < today_click_down) or enable_today_click:
							if act_user[uid] < act_hour or enable_act_hour:
								if (int(iitem[iid][3]) < item_0 and int(iitem[iid][2])<item_1 and int(iitem[iid][1])<item_2 and int(iitem[iid][0])<item_3) or enable_item:
									if (float(user_item[key])/float(user[uid][4]) > item_user_rate) or enable_item_user_rate:
										if iitem[iid][5] > 0.02 or enable_item_buy_rate:
										# if item_r.has_key(iid):
										# 	# if int(iitem[iid][3]) > 1:
										# 	# 	result[key] = 1
										# 	# print user_item[key]
										# 	print "========================="
										# else:
										# 	item_r[iid] = 1
										# 	result[key] = 1
											result[key] = 1

	# yestorday 23h: carted item
	for key in h23:
		uid, iid = key
		ckey = (uid, day1[key][2][0])

		if item.has_key(iid) and h23[key][0][2]>0 and h23[key][0][3]==0 and day1_c[ckey][0][3] == 0:
			result[key] = 1

# 	#filter
# 	catagary = {}
# 	for key in result:
# 		uid , iid = key
# 		cid = day1[key][2][0]
# 		ckey = (uid, cid)

# 		if catagary.has_key(ckey):
# 			catagary[ckey].append(key)
# 		else:
# 			catagary[ckey] = []
# 			catagary[ckey].append(key)

# 	for c in catagary:
# 		minn = catagary[c][0]
# #		print catagary[c]
# 		for each in catagary[c]:
# 			if day1[each][0][4] < day1[minn][0][4]:
# 				minn =  each
# 		if len(catagary[c])>2:
# 			catagary[c].remove(minn)
# 			result.pop(minn)
# 		print catagary[c]
# 		print "================================"
# 		minn = catagary[c][0]
# 		for each in catagary[c]:
# 			if day1[each][0][4] < day1[minn][0][4]:
# 				minn =  each
# 		if len(catagary[c])>2:
# 			catagary[c].remove(minn)
# 			result.pop(minn)

# 		minn = catagary[c][0]
# 		for each in catagary[c]:
# 			if day1[each][0][4] < day1[minn][0][4]:
# 				minn =  each
# 		if len(catagary[c])>2:
# 			catagary[c].remove(minn)
# 			result.pop(minn)

# 		minn = catagary[c][0]
# 		for each in catagary[c]:
# 			if day1[each][0][4] < day1[minn][0][4]:
# 				minn =  each
# 		if len(catagary[c])>2:
# 			catagary[c].remove(minn)
# 			result.pop(minn)


	f = open("../result/liyp_click_not_buy_predict_17.csv","wb")
	write = csv.writer(f)
	write.writerow(["user_id","item_id"])
	total = 0
	for key in result:
		write.writerow(key)
		total += 1
	print "generate submission file,total %d  (uid,iid)" %total
	f.close()


# model_one(0,	0, 			#today cart
# 	0,	0, 			#today buy
# 	0,	1, 11,			#today click 1----11
# 	0,	2, 40,			#today cata click 2-----40
# 	0,	0,			#today cata buy
# 	0,	95,			#user_act_hour
# 	0,	10,15,7,240,		#item
# 	0,	0.001,			#item_user_rate
# 	0,	0			#user_buy_rate
# 	)

# # model_one()
# CaculateF1("../result/user_item_buy_18.csv", "../result/liyp_click_not_buy_predict_17.csv")