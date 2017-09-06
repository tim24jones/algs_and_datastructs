def bubbleSort(alist): #going in both directions, useful for stacks
        for a in range (len(alist)//2):
            while (i+1<len(alist)):
                if alist[i]>alist[i+1]:
                    alist[i],alist[i+1]=alist[i+1],alist[i]
                i=i+2
            if len(alist%2==0:
                i=len(alist)-1
            else:
                i=len(alist)
            while (i>0):
                if alist[i]<alist[i-1]:
                    alist[i-1],alist[i]=alist[i],alist[i-1]