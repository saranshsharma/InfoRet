import numpy
import math
import random
import sys
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

                dataDict[buf[0]]=[buf[1],int(buf[2])]
                if buf[0] not in aUsrList:
                        aUsrList.append(buf[0])
                if buf[1] not in aBooksList:
                        aBooksList.append(buf[1])
                        #print buf
                i+=1
        #print dataList[0:10]
        return dataDict,aUsrList,aBooksList
def getCosineSim(a,b):
        asqr = a*a
        bsqr = b*b
        mul = a*b
        rx = float(math.sqrt(asqr.sum()))
        ry = float(math.sqrt(asqr.sum()))
        
        rxry = mul.sum()
        #print rx,ry,rxry
        if rx==0 or ry==0:
                if rx==0 and ry==0:
                        #print "chut"
                        return 1
                #print "lawda"
                return 0
        val = float(float(rxry)/(float(rx)*float(ry)))
        #print "val",val
        return val
def getItemCorMat(DataMat):
        usr_len,book_len=DataMat.shape
        print "Size of Datamat",DataMat.shape
        CorMat = numpy.zeros((book_len,book_len),numpy.dtype('f8'))
        for i in range(0,book_len-1):
                for j in range(i,book_len):
                        cosval = getCosineSim(DataMat[:,i],DataMat[:,j])
                        CorMat[i][j]=cosval
        return CorMat

def getCosPred(usrIndex,itemIndex,DataMat,CorMat):
        a,b = DataMat.shape
        userVect = numpy.zeros((b),numpy.dtype('f8'))
        itemVect = numpy.zeros((b),numpy.dtype('f8'))
        userVect = DataMat[usrIndex,:]
        itemVect = CorMat[:,itemIndex]
        mul = userVect*itemVect
        val = itemVect.sum()
        if val==0.0:
                return 0

        return float(mul.sum())/float(val)
############################################
filename = sys.argv[1]
size = int(sys.argv[2])
size2 = 100
testratio = 0.2
patho = sys.argv[3]
uid = int(sys.argv[4])
DataMat = getJesterMat(filename,size,size2)
testList = createTestList(DataMat,testratio)
out_file = patho+'\cos_out.txt'
out_user = patho+'\user_cos_out.txt'
fp2 = open(out_file,"w")
print DataMat
a,b = DataMat.shape
if uid != -1:
        fp3 = open(out_user,'w')
        

CorMat = getItemCorMat(DataMat)
print type(CorMat)
print">>>>>>>>>>>>>>>>>>>>>>>>>>>>"
print CorMat
print">>>>>>>>>>>CORMAT^^^>>>>>>>>>>>>>>>>>"
chck=size/2
notFounderr=0.0
Founderr=0.0
usrList={}
##print "check>>",DataMat[chck][chck]
for i in range(0,a):
        #print ">>>",i
        
        for j in range(0,b):
                if DataMat[i][j]==0:
                        predval = getCosPred(i,j,DataMat,CorMat)
                        
                        if predval !=0.0:
                                str1 = "user:"+' '+str(i)+' '+"item:"+' '+"predicted_value:"+' '+str(predval)+'\n'
                                #print "%s,%s == %s"%(i,j,predval)
                                fp2.write(str1)
                                err = testModule(i,j,predval,testList)
                                if err == -99:
                                        notFounderr+=1
                                else:
                                        Founderr+=err*err
                                if uid == i:
                                        #str2 = 'item:'+' '+str(j)+' '+'rating:'+' '+str(predval)+'\n'
                                        #fp3.write(str2)
                                        usrList[predval]=j
                        #print 
#Founderr=math.sqrt(Founderr)
print uid
sortedList=usrList.keys()
sortedList.sort()
sortedList = sortedList[::-1]
for x in sortedList:
        #print x, usrList[x]
        str2 = 'item:'+' '+str(usrList[x])+' '+'rating:'+' '+str(x)+'\n'
        fp3.write(str2)
print "and we are done"
print "Found error : ",Founderr
print "Founderr rate : ",math.sqrt(float(Founderr)/float(a*b*testratio))
print "NotFound error: ",notFounderr
print "notFounderr rate : ",float(notFounderr)/float(a*b*testratio)
#wait= raw_input()
#wait2=raw_input()
#a,b = CorMat.shape
##for i in range(0,a):
##        for j in range(0,b):
####                if i==j:
####                        print CorMat[i][j],"(%s,%s)"%(i,j)
####
####                else:
####                        print">%s<"%CorMat[i][j]
##                if CorMat[i][j]<1.0 and CorMat[i][j]>0.0:
##                        print CorMat[i][j],"(%s,%s)"%(i,j)
