class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        size=1
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          skippedslot=1
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            skippedslot=skippedslot+1
            nextslot = self.rehash(nextslot,skippedslot,len(self.slots))
          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,skippedslots,size):
        return (oldhash+skippedslots**2)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      skippedslot=1
      while self.slots[position] != None and  \
                           not found and not stop:
         skippedslot=skippedslot+1
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,skippedslot,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)
