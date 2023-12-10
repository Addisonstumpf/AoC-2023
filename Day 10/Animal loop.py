import time
f = open(r"Day 10\input.txt","r")
#f = open(r"Day 10\sample.txt","r")

lines = []
answerOne = 0
answerTwo = 0

for x, line in enumerate(f):
    wl = []
    line = line.rstrip()
    for i in range(len(line)):
        wl.append(line[i])
    lines.append(wl)
    if line.find('S') != -1:
        startRow = x
        startCol = line.find('S')

#   1
#  2 3
#   4


up = [startRow-1, startCol, 4]
down = [startRow+1, startCol, 1]
left = [startRow, startCol-1, 3]
right = [startRow, startCol+1, 2]
print (up, down, left, right)

def step(map, point):
    opts={'|':[1,4], '-':[2,3], 'L':[1,3], 'J':[1,2], '7':[2,4], 'F':[3,4]}
    if point[0]==-1 or point[1]==-1:
        return [-1,-1,-1]
    if map[point[0]][point[1]]=='.':
        return [-1,-1,-1]
    opt = opts[map[point[0]][point[1]]]
    if opt[0]==point[2]:
        outDir=opt[1]
    else:
        if opt[1]==point[2]:
            outDir=opt[0]
        else:
            return [-1, -1, -1]
    if outDir ==1:
        if point[0] ==0:
            return [-1,-1,-1]
        return [point[0]-1, point[1], 4]
    if outDir ==2:
        if point[1]==0:
            return [-1,-1,-1]
        return[point[0], point[1]-1, 3]
    if outDir ==3:
        if point[1]==len(map[0])-1:
            return [-1,-1,-1]
        return [point[0], point[1]+1, 2]
    if outDir ==4:
        if point[0]==len(map)-1:
            return [-1,-1,-1]
        return [point[0]+1, point[1], 1]

thereYet = False
stepCount = 0
while not thereYet:
    up = step(lines, up)
    down = step(lines, down)
    left = step(lines, left)
    right = step(lines, right)
    stepCount +=1
    if lines[up[0]][up[1]] == 'S' or \
       lines[down[0]][down[1]] == 'S' or \
       lines[left[0]][left[1]] == 'S' or \
       lines[right[0]][right[1]] == 'S':
        thereYet = True

answerOne = (stepCount+1)/2
lines[startRow][startCol] = 'F'

def fillOut(map, loop, point):
    dirs =[False, False, False, False]
    cont = True
    match map[point[0]][point[1]]:
        case 'F':
            if point[2] == 3:
                dirs[0]=True
                dirs[1]=True
        case '7':
            if point[2] == 4:
                dirs[0]=True
                dirs[2]=True
        case 'L':
            if point[2] == 1:
                dirs[1]=True
                dirs[3]=True
        case 'J':
            if point[2] == 2:
                dirs[2]=True
                dirs[3]=True
        case '-':
            if point[2] == 2:
                dirs[3]=True
            else:
                dirs[0]=True
        case '|':
            if point[2] == 1:
                dirs[1]=True
            else:
                dirs[2]=True
    if dirs[0]:
        loop,cont = enclose(loop, [point[0]-1, point[1]])
        if not cont:
            print(dirs)
            return loop, cont
    if dirs[1]:
        loop,cont = enclose(loop, [point[0], point[1]-1])
        if not cont:
            print(dirs)
            return loop, cont
    if dirs[2]:
        loop,cont = enclose(loop, [point[0], point[1]+1])
        if not cont:
            print(dirs)
            return loop, cont
    if dirs[3]:
        loop,cont = enclose(loop, [point[0]+1, point[1]])
        if not cont:
            print(dirs)
            return loop, cont
    return loop, cont

def enclose(loop, point):
    
    if loop[point[0]][point[1]] in ['X', 'I']:
        return loop, True
    if point[0]==0 or point[1]==0 or point[0]==len(loop)-1 or point[1]==len(loop[0])-1:
        loop[point[0]][point[1]] = 'I'
        return loop, False
    else:
        loop[point[0]][point[1]] = 'I'
        cont = True
        if loop[point[0]-1][point[1]]=='.':
            loop,cont = enclose(loop, [point[0]-1, point[1]])
        if cont and loop[point[0]+1][point[1]]=='.':
            loop,cont = enclose(loop, [point[0]+1, point[1]])
        if cont and loop[point[0]][point[1]-1]=='.':
            loop,cont = enclose(loop, [point[0], point[1]-1])
        if cont and loop[point[0]][point[1]+1]=='.':
            loop,cont = enclose(loop, [point[0], point[1]+1])
    return loop, cont

justLoop=[]
for i in range(len(lines)):
    wRow = []
    for j in range(len(lines[i])):
        wRow.append('.')
    justLoop.append(wRow)
justLoop[startRow][startCol]='X'
down = step(lines, down)
loopCount =0
cont = True
while down[0] !=startRow or down[1] != startCol or loopCount ==0:
    if down[0]==startRow and down[1]==startCol:
        loopCount = 1
    if loopCount == 0:
        justLoop[down[0]][down[1]] = 'X'    
    else:
        if down == [113, 18, 1]:
            pass
        justLoop, cont = fillOut(lines, justLoop, down)
        

    if not cont:
        break
    down = step(lines, down)
outStr = ''
for i in range(len(justLoop)):
    wStr = ''
    for j in range(len(justLoop[i])):
        wStr+= justLoop[i][j]
        wStr+= ' '
    outStr+=wStr
    outStr +='\n'

print (outStr)
for i in range(len(justLoop)):
    for j in range(len(justLoop[i])):
        if justLoop[i][j] == 'I':
            answerTwo+=1

print(answerOne)
print(answerTwo)
print (time.process_time())