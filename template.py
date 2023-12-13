import time

def TTC(iList):
    outStr = ''
    for i in range(len(iList)):
        wStr = ''
        for j in range(len(iList[i])):
            wStr+= iList[i][j]
            wStr+= ' '
        outStr+=wStr
        outStr +='\n'
    return outStr

f = open(r"Day X\input.txt","r")
#f = open(r"Day X\sample.txt","r")

lines = []
answerOne = 0
answerTwo = 0

for line in f:
    #do the thing
    #list(map(int, item.rstrip().split(' ')))

print(answerOne)
print(answerTwo)
print (time.process_time())