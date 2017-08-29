def max_digits(list):
    max=int(list[0])
    for anumber in list:
        if max<int(anumber):
            anumber=max
    max_digits=(max_element(list)%10)+1
    return max_digits

def radix_sort(list)
    for n in range max_digits:
        for m in range(10):
            for i in range(len(list):
                list=[list[i]//(n*10)%10==m]+[list[i]//(n*10)%10!=m]
radix_sort([2,15,3,1,7])           