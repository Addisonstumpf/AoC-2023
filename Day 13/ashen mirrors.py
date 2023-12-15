import time

# def TTC(iList):
#     outStr = ''
#     for i in range(len(iList)):
#         wStr = ''
#         for j in range(len(iList[i])):
#             wStr+= iList[i][j]
#             wStr+= ' '
#         outStr+=wStr
#         outStr +='\n'
#     return outStr

f = open(r"Day 13\input.txt","r")
#f = open(r"Day 13\sample.txt","r")

lines = []
answerOne = 0
answerTwo = 0

def row(list, num):
    if num >= len(list):
        return None
    return list[num]

def col(list, num):
    if num >=len(list[0]):
        return None
    answer = []
    for i in list:
        answer.append(i[num])
    return answer

def dist(A, B):
    answer = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            answer +=1
    return answer

def findReflection(list, smudge):
    success = 0
    for i in range(1, len(list), 2):
        if dist(row(list, 0), row(list, 0+i))<=smudge:
            for j in range(0, (i+1)//2, 1):
                success +=dist(row(list, 0+j), row(list, 0+i-j))
            if success == smudge:
                return 100*(i+1)//2
            success = 0
    k=len(list)-1
    for i in range(1, len(list), 2):
        if dist(row(list, k), row(list, k-i))<=smudge:
            for j in range(0, (i+1)//2, 1):
                success+= dist(row(list, k-j), row(list, k-i+j))
            if success == smudge:
                return 100*(2*k-i+1)//2
            success = 0
    for i in range(1, len(list[0]), 2):
        if dist(col(list, 0), col(list, 0+i))<=smudge:
            for j in range(0, (i+1)//2, 1):
                success +=dist(col(list, 0+j), col(list, 0+i-j))
            if success == smudge:
                return (i+1)//2
            success = 0
    k=len(list[0])-1
    for i in range(1, len(list[0]), 2):
        if dist(col(list, k), col(list, k-i))<=smudge:
            for j in range(0, (i+1)//2, 1):
                success+= dist(col(list, k-j), col(list, k-i+j))
            if success == smudge:
                return (2*k-i+1)//2
            success = 0
            


grid = []
for line in f:
    line = line.rstrip()
    if len(line) > 0:
        gLine = []
        for i in range(len(line.rstrip())):
            gLine.append(line[i])
        grid.append(gLine)
    else:
        answerOne += findReflection(grid, 0)
        answerTwo += findReflection(grid, 1)
        grid = []
answerOne += findReflection(grid,0)
answerTwo += findReflection(grid, 1)

print(answerOne)
print(answerTwo)
print (time.process_time())