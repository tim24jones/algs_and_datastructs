the_list=[1,2,3,4,5,6,7]
def reverse(input_list):
    newlist=[]
    for i in range(len(input_list)):
        newlist=[input_list[i]]+newlist
    return newlist
print(reverse(the_list))