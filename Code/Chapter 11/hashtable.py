class HashTable:
    def __init__(self,size=11,lf=0.8,probfunc='linear',hkc=8):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.fslots = 0
        self.lfLimit = lf
        self.prob = ['linear','quad','double']
        self.probfunc = probfunc
        self.hashkeyconstant = hkc

    def set2ndhkc(self,hkc):
        assert hkc > 0 or hkc <= 100, "Invalide value!, Please provide value between 1 and 100"
        self.hashkeyconstant = hkc

    def get2ndhkc(self):
        return self.hashkeyconstant

    def setprobfunc(self,pf):
        assert pf in ['linear','quad','double'], "Invalide value!, Please provide one of the method in {linear, quad, double}"
        self.probfunc = pf

    def getprobfunc(self):
        return self.probfunc

    def setLF(self,value):
        assert value>0 or value<=100, "Invalide value!, Please provide value in percentage (e.g. between 1 and 100)"
        self.lfLimit = value/100

    def getLF(self):
        return self.lfLimit

    def add(self, data):
        if self.probfunc == 'linear':
            return self.add1(data)
        elif self.probfunc == 'quad':
            self.add2(data)
        else:
            self.add3(data)

    def add1(self, data):
        hashvalue = self.hashfunction(data, self.size)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = hashvalue
            self.data[hashvalue] = data
            self.fslots +=1
            lf = self.loadFactor(self.fslots)
            if lf>=self.lfLimit:
                self.extendHashSize()

        elif self.fslots<self.size:
            nextslot = self.rehash(hashvalue,self.size)
            if self.slots[nextslot]==None:
                self.slots[nextslot] = nextslot
                self.data[nextslot] = data
                self.fslots += 1
                lf = self.loadFactor(self.fslots)
                if lf >= self.lfLimit:
                    self.extendHashSize()
            else:
                while self.slots[nextslot]!=None and nextslot!=hashvalue:
                    nextslot = self.rehash(nextslot,self.size)
                if nextslot!=hashvalue:
                    self.slots[nextslot] = nextslot
                    self.data[nextslot] = data
                    self.fslots += 1
                    lf = self.loadFactor(self.fslots)
                    if lf >= self.lfLimit:
                        self.extendHashSize()

    def add2(self,data):
        i=1
        home = self.hashfunction(data, self.size)
        if self.slots[home] == None:
            self.slots[home] = home
            self.data[home] = data
            self.fslots += 1
            lf = self.loadFactor(self.fslots)
            if lf >= self.lfLimit:
                self.extendHashSize()

        elif self.fslots < self.size:
            nextslot = self.quadProb(home, i)
            if self.slots[nextslot] == None:
                self.slots[nextslot] = nextslot
                self.data[nextslot] = data
                self.fslots += 1
                lf = self.loadFactor(self.fslots)
                if lf >= self.lfLimit:
                    self.extendHashSize()
            else:
                while self.slots[nextslot] != None and nextslot != home:
                    i+=1
                    nextslot = self.quadProb(home,i)
                if nextslot != home:
                    self.slots[nextslot] = nextslot
                    self.data[nextslot] = data
                    self.fslots += 1
                    lf = self.loadFactor(self.fslots)
                    if lf >= self.lfLimit:
                        self.extendHashSize()

    def add3(self,data):
        i=1
        home = self.hashfunction(data, self.size)
        if self.slots[home] == None:
            self.slots[home] = home
            self.data[home] = data
            self.fslots += 1
            lf = self.loadFactor(self.fslots)
            if lf >= self.lfLimit:
                self.extendHashSize()

        elif self.fslots < self.size:
            nextslot = self.dhashing(home, i)
            if self.slots[nextslot] == None:
                self.slots[nextslot] = nextslot
                self.data[nextslot] = data
                self.fslots += 1
                lf = self.loadFactor(self.fslots)
                if lf >= self.lfLimit:
                    self.extendHashSize()
            else:
                while self.slots[nextslot] != None and nextslot != home:
                    i+=1
                    nextslot = self.dhashing(home,i)
                if nextslot != home:
                    self.slots[nextslot] = nextslot
                    self.data[nextslot] = data
                    self.fslots += 1
                    lf = self.loadFactor(self.fslots)
                    if lf >= self.lfLimit:
                        self.extendHashSize()


    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def quadProb(self,home,i):
        return (home+(i**2)) % self.size

    def dhashing(self,key,i):
        home = key % self.size
        hp = 1 + (key % self.hashkeyconstant)
        return (home+(i*hp)) % self.size

    def loadFactor(self,fslot):
        return fslot/self.size

    def extendHashSize(self):
        tmpdata = self.data
        self.size = (2*self.size)+1
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.fslots = 0
        for item in tmpdata:
            if item!=None:
                self.add1(item)

    def searchKey(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            #print(self.slots[position])
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def searchItem(self, item):
        startslot = self.hashfunction(item, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.data[position] != None and \
                not found and not stop:
            #print(self.data[position])
            if self.data[position] == item:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.data))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.add1(key, data)

    def __len__(self):
        return self.size




