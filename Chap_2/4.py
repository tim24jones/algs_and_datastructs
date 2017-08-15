def mergeSort(list):
    if len(list<=1:
        return list #list so short it is already sorted
    else:
        mid=k//2
        lefthalf=initlist[:mid]
        righthalf=initlist[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        x=0
        y=0
        z=0
        while x<len(lefthalf) and y<len(righthalf):
            if lefthalf[x]<righthalf[y]:
                initlist[z]=lefthalf[x]
                x=x+1
            else:
                initlist[z]=righthalf[y]
                y=y+1
            z=z+1

        while x<len(lefthalf):
            initlist[z]=lefthalf[x]
            x=x+1
            z=z+1

        while y<len(righthalf):
            initlist[z]=righthalf[y]
            y=y+1
            z=z+1
def main():
    sorted=mergesort(list) #sort the list
    return sorted[k+1]  #pick out the kth smallest element, add 1 because index starts at zero