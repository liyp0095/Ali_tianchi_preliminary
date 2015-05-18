import os
import csv
import cPickle

from sys import path
path.append(r"../rule")
path.append(r"../howtoknow")
path.append(r"../queuing")

from our_model import model_one
from caculateF1 import CaculateF1

model_one(0,	0, 			#today cart
	0,	0, 			#today buy
	0,	2, 11,			#today click 1----11
	0,	2, 40,			#today cata click 2-----40
	0,	0,			#today cata buy
	0,	95,			#user_act_hour
	0,	10,15,7,240,		#item
	0,	0.002,			#item_user_rate
	0,	0.05			#item_buy_rate
	)

CaculateF1("0.05", "../result/17_18_wrong.csv", "../result/user_item_buy_18.csv", "../result/liyp_click_not_buy_predict_17.csv")


# result = [1,2,3,4]
# f = open("../result/test.csv","ab")
# write = csv.writer(f)
# write.writerow(["user_id","item_id"])
# # total = 0
# # for key in result:
# # 	write.writerow(key)
# # 	total += 1
# # print "generate submission file,total %d  (uid,iid)" %total
# f.close()