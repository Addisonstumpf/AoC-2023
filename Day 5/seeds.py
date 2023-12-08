class mapList(list):
    #set up properties
    @property
    def curs(self):
        return self._curs
    @curs.setter
    def curs(self,value:int):
        if value >=0 and value <= len(self)-1:
            self._curs = value
        else:
            self._curs = -1

    @property
    def inStart(self):
        return self[self.curs][0]
    
    @property
    def outStart(self):
        return self[self.curs][1]
    
    @property
    def dist(self):
        return self[self.curs][2]
    #this needs a better name, "first"-ness makes sense if you're doing composition, but you also need it for evaluation, where it doesn't.
    @property
    def first(self):
        return self._first
    
    @first.setter
    def first(self, value:bool):
        self._first = value

    #is a value inside the range of the row defined by the cursor? 
    def within(self, value) -> bool:
        if self.curs == -1:
            return False
        if self.first:
            if int(value)>=self.outStart and int(value) < self.outStart+self.dist:
                return True
            else:
                return False
        else:
            if int(value)>=self.inStart and int(value) < self.inStart+self.dist:
                return True
            else:
                return False

    #what's the output of this map for a value?
    def evaluate(self, value):
        self.first = False
        value = int(value)
        self.sort(key=lambda x: x[0])
        self.curs = 0
        while self.inStart<=value:
            self.curs+=1
            if self.curs ==-1:
                return value
        self.curs-=1
        if self.within(value):
            return self.outStart+value-self.inStart
        else:
            return value

    #from this value, where's the next interesting event for the row defined by the cursor?
    def nextPointOfInterest(self, value):
        value=int(value)
        if self.curs ==-1:
            return 0
        if self.first:
            if value>=self.outStart and value < self.outStart+self.dist:
                return self.outStart+self.dist
            elif value <self.outStart:
                return self.outStart
            else:
                raise ValueError
        else:
            if value>=self.inStart and value < self.inStart+self.dist:
                return self.inStart+self.dist
            elif value < self.inStart:
                return self.inStart
            else:
                raise ValueError

    #slight shortcut to the norm
    def append(self, inStart:int, outStart:int, dist:int):
        super().append((int(inStart),int(outStart),int(dist)))

    #returns the map resulting from applying this map, and then the map in other. 
    #if destructive, it only returns the portions of that map corresponding to mapped areas in the first map.
    def compose(self, other, destructive:bool=False):
        answer = mapList()
        self.sort(key=lambda x: x[1])
        self.first = True
        self.curs = 0
        other.sort(key=lambda x: x[0])
        other.first = False
        other.curs = 0
        x=min(self.outStart, other.inStart)
        while self.curs !=-1 or other.curs !=-1:
            if self.curs == -1:
                y= other.nextPointOfInterest(x)
            elif other.curs == -1:
                y=self.nextPointOfInterest(x)
            else:
                y=min(self.nextPointOfInterest(x), other.nextPointOfInterest(x))
            if self.within(x):
                if other.within(x):
                    answer.append(self.inStart+x-self.outStart, other.outStart+x-other.inStart, y-x)
                else:
                    answer.append(self.inStart+x-self.outStart, x, y-x)
            else:
                if not destructive:
                    if other.within(x):
                        answer.append(x, other.outStart+x-other.inStart, y-x)
            if y==self.nextPointOfInterest(x) and self.within(x):
                self.curs+=1
            if y==other.nextPointOfInterest(x) and other.within(x):
                other.curs+=1
            x=y
        return answer

f = open(r"Day 5\input.txt","r")
#f = open(r"Day 5\sample.txt","r")

modes = ['seed-', 'soil-', 'ferti', 'water', 'light', 'tempe', 'humid']

totalMap = None
buildMap = mapList()
answerOne = 0
answerTwo = 0
mode = -1

for line in f:
    if len(line)<4:
        #we've finished building a mapping, now compose it into the total.
        mode = 0
        if totalMap:
            totalMap, buildMap = totalMap.compose(buildMap),mapList()
        else:
            totalMap, buildMap = buildMap, mapList()
    if mode ==-1:
        #get seed list
        seedList = line.split(' ')
        pass
    elif mode == 1:
        #we're in a mapping
        mapLine = line.split(' ')
        buildMap.append(mapLine[1], mapLine[0], mapLine[2])
    elif mode == 0:
        if line[0:5] in modes:
            #this is a header for a new map
            mode=1
#we've finished building the last map, compose it in
totalMap, buildMap = totalMap.compose(buildMap), None
#use that to get the outputs for the given seeds, and find minimum.
seedVals = []
for seed in seedList:
    if seed !='seeds:':
        seedVals.append(totalMap.evaluate(seed))
answerOne = min(seedVals)
#oops seedList needs to be turned into a reflexive map
i = 1
seedMap = mapList()
while i<len(seedList):
    seedMap.append(seedList[i], seedList[i], seedList[i+1])
    i+=2
#compose one last time, destructively
totalMap = seedMap.compose(totalMap, True)
#now just find the lowest output value
totalMap.sort(key=lambda x: x[1])
answerTwo = totalMap[0][1]
print(answerOne)
print(answerTwo)