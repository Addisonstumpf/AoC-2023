import time
f = open(r"Day 11\input.txt","r")
#f = open(r"Day 11\sample.txt","r")

lines = []
galaxies = []
answerOne = 0
answerTwo = 0

for x, line in enumerate(f):
    line = line.rstrip()
    wRow = []
    if x == 0:
        colExp =[True]*len(line)
        rowExp = []
    thisRow = True
    for i in range(len(line)):
        wRow.append(line[i])
        if line[i]=='#':
            colExp[i]=False
            thisRow = False
    lines.append(wRow)
    rowExp.append (thisRow)

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j]=='#':
            galaxies.append([i,j])

def dist(A, B, rowExp, colExp, expand):
    crossing = 0
    sRow = min(A[0], B[0])
    while sRow != max(A[0], B[0]):
        if rowExp[sRow]:
            crossing+=1
        sRow+=1
    sCol = min(A[1], B[1])
    while sCol != max(A[1], B[1]):
        if colExp[sCol]:
            crossing+=1
        sCol+=1
    answer = abs(A[0]-B[0])+abs(A[1]-B[1])+crossing*expand
    return answer

for i in range(len(galaxies)):
    for j in range(len(galaxies)-i):
        #print (i+1, ',',  i+j+1, dist(galaxies[i], galaxies[i+j]))
        answerOne+=dist(galaxies[i], galaxies[i+j], rowExp, colExp, 1)
        answerTwo+=dist(galaxies[i], galaxies[i+j], rowExp, colExp, 999999)

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


print(answerOne)
print(answerTwo)
print (time.process_time())