def binarySearch_recursive(alist,item):
    if len(alist)==0:
        return False
    else:
        midpoint=len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                for i in range(midpoint):
                    newlist[i]=alist[i]
                return binarySearch_recursive(newlist,item)
            else:
                for i in range(midpoint+1,len(alist))
                    newlist[len(alist)-midpoint+1+i]=alist[i]
                return binarySearch_recursive(newlist,item)