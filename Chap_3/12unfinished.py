from pythonds.basic.deque import Deque

def palchecker(aString):
    chardeque = Deque()
    newString=aString.replace(' ','')
    for ch in newString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
