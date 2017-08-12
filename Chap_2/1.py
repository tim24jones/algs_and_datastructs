import random
import time
mylist=[]
for m in range(1000):
    mylist=mylist+[random.randint(0,99)*10] #create mylist containing random integers
    #print(mylist)
    indx=random.randint(0,len(mylist)-1) #select random index placement
    #print(indx)
    start=time.time()
    mylist[indx]
    end=time.time()
    length=end-start
    print(length/(indx+1), '\t',length/(len(mylist)+1))