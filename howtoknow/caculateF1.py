#-*-coding:utf-8-*-#
"""
caculate F1 value for your answer

"""

import os
import csv

def CaculateF1(jieguo,F1_file, std_result_file, your_answer_file):
    file1 = open(std_result_file)
    std_result = csv.reader(file1)
    std_result.next()
    dictionary = {}
    res_count = 0
    for row in std_result:
        res_count += 1
        uid = row[0]
        iid = row[1]
        key = (uid, iid)
        dictionary[key] = 1
    #存储 (uid,iid)
    # result = {}

    file2 = open(your_answer_file)
    your_answer = csv.reader(file2)
    your_answer.next()
    ans_count = 0
    correct = 0
    for row in your_answer:
        ans_count += 1
        user_id = row[0]
        item_id = row[1]
        if dictionary.has_key((user_id, item_id)):
#            print user_id,item_id
            correct += 1
    if ans_count == 0:
        print '000000000000000000000000000000000000000'
        return        
            
    P = 100*float(correct)/ans_count
    R = 100*float(correct)/res_count
    if correct != 0:
        f1 = 2*P*R/(P+R)
    else:
        f1 = 0

    print "======================================"
    print "std_result: %d" %res_count
    print "your_answer: %d" %ans_count
    print "correct: %d" %correct
    print "correct Radio: %f" %P
    print "recall Radio: %f" %R
    print "F1: %f" %f1
    print "======================================"

    if os.path.exists(F1_file):
        first = 0
    else:
        first = 1
    f = open(F1_file,"ab")
    write = csv.writer(f)
    if(first):
        write.writerow(["","std_result","your_answer","correct","correct Radio","recall Radio","F1"])
    write.writerow([jieguo,res_count, ans_count, correct, round(P, 2), round(R, 2), round(f1, 2)])
# total = 0
# for key in result:
#   write.writerow(key)
#   total += 1
# print "generate submission file,total %d  (uid,iid)" %total
    f.close()

#CaculateF1("../result/user_item_buy_18.csv", "../data/test/tlast177.csv")


# item = cPickle.load(open("../data/dictionary/item.pkl","rb"))  #商品子集，19号购买商品所在集
# day = cPickle.load(open("../data/dictionary/date/2014-12-17.pkl","rb"))

# for key in day:
#     uid,iid = key
#     #对于商品子集里的商品，18号加购物车且没买的，生成提交文件
#     if  item.has_key(iid) and day[key][0][2]>0 and day[key][0][3]==0:
#         # rows = csv.reader(open("../data/user/"+key[0]+".csv","rb"))
#         # rows.next()           
#         # for row in rows:
#         #     if row[0] == "2014-12-18" and row[1] == key[1] and row[2] == "3":
#                result[key] = 1



# #写入文件
# f = open("../result/tianchi_mobile_recommendation_predict_17.csv","wb")
# write = csv.writer(f)
# write.writerow(["user_id","item_id"])
# total = 0
# for key in result:
#     write.writerow(key)
#     total += 1 
# print "generate submission file,total %d  (uid,iid)" %total
# f.close()
