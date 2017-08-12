import random
import time
mydict={0:23}
mylist=[0]
for m in range(1000):
    mydict[m+1]=random.randint(0,99)
    mylist=mylist+[random.randint(0,99)]+[random.randint(0,99)]
    mydict[-1*(m+1)]=random.randint(0,99)  #create mydict containing random integers
    print(mydict)
    print(mylist)
    k=random.randint(0,999)
    dictstart=time.time()
    del mydict[m-1]
    dictend=time.time()
    liststart=time.time()
    del mylist[-1]
    listend=time.time()
    listlength=listend-liststart
    dictlength=dictend-dictstart
    print(listlength,dictlength)