import CosSimJester
import UserJester
import numpy
import sys
import random
import math

filename = sys.argv[1]
size = int(sys.argv[2])
size2 = 50
patho = sys.argv[3]
uid = int(sys.argv[4])
out_file = patho+'\hybrid_out.txt'
out_user = patho+'\user_hybrid_out.txt'
fp2 = open(out_file,"w")
if uid != -1:
    fp3 = open(out_user,'w')
        
DataMat=UserJester.getJesterMat(filename,size,size2)
CorMat = CosSimJester.getItemCorMat(DataMat)
a,b= DataMat.shape
testratio = 0.2
testList = UserJester.createTestList(DataMat,testratio)
notFounderr=0.0
Founderr=0.0
usrList={}
for i in range(0,a):
    for j in range(0,b):
        if UserJester.DataMat[i][j] == 0.0:
            pred_val1 = UserJester.pred(i,j,DataMat,size2)
            pred_val2 = CosSimJester.getCosPred(i,j,DataMat,CorMat)
            pred_val = (pred_val1+pred_val2)/2
            if pred_val != 0.0 and pred_val >= -10 and pred_val <= 10:
                #print "%s %s = %s"%(i,j,pred_val)
                str1 = "user:"+' '+str(i)+' '+"item:"+' '+str(j)+' '+"predicted_value:"+' '+str(pred_val)+'\n'
                fp2.write(str1)
                err = UserJester.testModule(i,j,pred_val,testList)
                if err == -99:
                    notFounderr+=1
                else:
                    Founderr+=err*err
                if uid == i:
                    #str2 = 'item:'+' '+str(j)+' '+'rating:'+' '+str(pred_val)+'\n'
                    #fp3.write(str2)
                    usrList[pred_val]=j

sortedList=usrList.keys()
sortedList.sort()
sortedList = sortedList[::-1]
for x in sortedList:
    #print x, usrList[x]
    str2 = 'item:'+' '+str(usrList[x])+' '+'rating:'+' '+str(x)+'\n'
    fp3.write(str2)

print usrList
print "and we are done"
print "Found error : ",Founderr
print "Founderr rate : ",math.sqrt(float(Founderr))/float(a*b*testratio)
print "NotFound error: ",notFounderr
print "notFounderr rate : ",float(notFounderr)/float(a*b*testratio)
