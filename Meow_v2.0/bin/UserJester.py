import numpy
import math
import random
import sys

def getJesterMat(filename,size,size2):

    DataMat = numpy.zeros((size,size2),numpy.dtype('f8'))
    fptr = open(filename,'r')
    buf = fptr.readline().strip().split(",")
    iteri = 0
    hit =0
    while iteri<size:
            for i in range(1,size2):
                    if buf[i] != "99":
                            DataMat[iteri][i-1]=float(buf[i])
                            
                            #print iteri,i-1
                    else:
                            #print "............"
                            hit+=1
            buf = fptr.readline().strip().split(",")
            iteri+=1
    print hit,size,size2
    return DataMat
def createTestList(dataMat,testratio):

    a,b=dataMat.shape
    hit = a*b*testratio
    testList = []
    while hit>=0:
            i = random.randint(0,a-1)
            j = random.randint(0,b-1)
            #print i,j
            if dataMat[i][j]!=0.0:
                 testList.append([i,j,dataMat[i][j]])
                 dataMat[i][j]=0.0
                 hit-=1
    return testList
def testModule(a,b,predval,testList):
    for x in testList:
        if x[0]==a and x[1]==b:
            err = float(predval-x[2])
            return err

    return -99

def getDataDict(filename,size):
    
    fptr = open(filename,'r')
    buf = fptr.readline()
    dataDict = {}
    aUsrList=[]
    aBooksList=[]
    indexList=[]
    i = 0
    while i<size:
            
            tempbuf = fptr.readline().strip().split(";")
            buf = [x.strip("\"") for x in tempbuf]
            #dataList.append([buf[0],buf[1],int(buf[2])])
            dataDict[buf[0]]=[buf[1],int(buf[2])]
            if buf[0] not in aUsrList:
                    aUsrList.append(buf[0])
            if buf[1] not in aBooksList:
                    aBooksList.append(buf[1])
                    #print buf
            i+=1
    #print dataList[0:10]
    return dataDict,aUsrList,aBooksList

def sim(a,b,DataMat,size2):
    a_avg = avgValUser(a,DataMat,size2)
    b_avg = avgValUser(b,DataMat,size2)
    mul_sum = 0
    sq_r1_sum = 0
    sq_r2_sum = 0
    for i in range(0,size2):
        if DataMat[a][i] != 0 and DataMat[b][i] != 0:
            r1 = DataMat[a][i] - a_avg
            r2 = DataMat[b][i] - b_avg
            mul_sum+=r1*r2
            sq_r1_sum += r1*r1
            sq_r2_sum += r2*r2
    if sq_r1_sum==0 or sq_r2_sum==0:
            return -100
    return (mul_sum/((math.sqrt(sq_r1_sum)*(math.sqrt(sq_r2_sum)))))

def avgValUser(user_id,DataMat,size2):
    usr_sum=0
    usr_len=0
    for i in range(0,size2):
        if DataMat[user_id][i] != 0:
            usr_sum += DataMat[user_id][i]
            usr_len += 1
    if usr_len == 0:
        return -99
    return usr_sum/usr_len

def pred(a,p,DataMat,size2):
    r1=0
    sim_sum=0
    for i in range(0,(size2-1)):
        if i == a:
            continue
        if DataMat[i][p] != 0:
            avg_rb = avgValUser(i,DataMat,size2)
            sim_val = sim(a,i,DataMat,size2)
            if sim_val==-100:
                continue
            r1 += (DataMat[i][p]-avg_rb)*sim_val
            sim_sum+=sim_val
    ra_avg=avgValUser(a,DataMat,size2)
    if sim_sum==0:
            return -101
    
    pred_ra = ra_avg+(r1/sim_sum)
    return pred_ra
    
############################################################################
filename = sys.argv[1]
size = int(sys.argv[2])
size2 = 50
patho = sys.argv[3]
uid = int(sys.argv[4])
out_file = patho+'\pear_out.txt'
out_user = patho+'\user_pear_out.txt'
fp2 = open(out_file,"w")
if uid != -1:
    fp3 = open(out_user,'w')
        

#dataDict,aUsrList,aBooksList=getDataDict(filename,size)
DataMat = getJesterMat(filename,size,size2)
a,b = DataMat.shape
#print DataMat
testratio = 0.2
testList = createTestList(DataMat,testratio)
notFounderr=0.0
Founderr=0.0
usrList={}
for i in range(0,a):
    for j in range(0,b):
        if DataMat[i][j] == 0.0:
            pred_val=pred(i,j,DataMat,size2)
            if pred_val != 0.0 and pred_val != -101 :
                #print "%s %s = %s"%(i,j,pred_val)
                str1 = "user:"+' '+str(i)+' '+"item:"+' '+"predicted_value:"+' '+str(pred_val)+'\n'
                fp2.write(str1)
                err = testModule(i,j,pred_val,testList)
                if err == -99:
                    notFounderr+=1
                else:
                    Founderr+=err*err
                if uid == i:
                    #str2 = 'item:'+' '+str(j)+' '+'rating:'+' '+str(pred_val)+'\n'
                    #fp3.write(str2)
                        #print
                    usrList[pred_val]=j
#Founderr=math.sqrt(Founderr)
sortedList=usrList.keys()
sortedList.sort()
sortedList = sortedList[::-1]
for x in sortedList:
    #print x, usrList[x]
    str2 = 'item:'+' '+str(usrList[x])+' '+'rating:'+' '+str(x)+'\n'
    fp3.write(str2)
print "and we are done"
print "Found error : ",Founderr
print "Founderr rate : ",math.sqrt(float(Founderr))/float(a*b*testratio)
print "NotFound error: ",notFounderr
print "notFounderr rate : ",float(notFounderr)/float(a*b*testratio)

        
