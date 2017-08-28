from pythonds.basic.queue import Queue
import random

def hotPotato(namelist, max_numrange):
    if max_numrange<1:
        return 'max_numrange is too small'
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(random.randint(1,max_numrange)):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))