import random
import time
mydict={}
value=0
nextvalue=0
for m in range(1000):
    mydict['m']=random.randint(0,99) #create mydict containing random integers
    print(mydict)
    k=random.randint(0,999)
    start=time.time()
    mydict.get(k)
    end.time.time()
    length=end-start
    print(length/k,)