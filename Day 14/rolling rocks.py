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

f = open(r"Day 14\input.txt","r")
#f = open(r"Day 14\sample.txt","r")

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

def load(list) -> int:
    answer = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == 'O':
                answer += len(list)-i
    return answer

def rollOne(list, forward:bool):
    if forward:
        i=len(list)-1
        while i >= 0:
            if list[i] != 'O' or i == len(list)-1:
                i -= 1
            else:
                if list[i+1] == '.':
                    list[i+1] = 'O'
                    list [i] = '.'
                    i += 1
                else:
                    i -= 1
    else:
        i=0
        while i <len(list):
            if list[i] != 'O' or i == 0:
                i += 1
            else:
                if list[i-1] == '.':
                    list[i-1] = 'O'
                    list [i] = '.'
                    i -= 1
                else:
                    i +=1
    return list
                
def rollAll(list, dir):
    if dir == 1 or dir == 4:
        for j in range(len(list[0])):
            work = col(list, j)
            if dir == 1:
                work = rollOne(work, False)
            else:
                work = rollOne(work, True)
            for i in range(len(work)):
                list[i][j] = work[i]
    else:
        for i in range(len(list)):
            work = row(list, i)
            if dir == 2:
                work = rollOne(work, False)
            else:
                work = rollOne(work, True)
            for j in range(len(work)):
                list[i][j] = work[j]
    return list

def spin(grid, period, target):
    affirmation = 0
    record = [load(grid)]
    while affirmation<100*period:
        grid = rollAll(grid, 1)
        grid = rollAll(grid, 2)
        grid = rollAll(grid, 4)
        grid = rollAll(grid, 3)
        record.append(load(grid))
        if len(record)>period:
            if record[-1] == record[-1-period]:
                affirmation +=1
            else:
                affirmation = 0
    i=len(record)-1
    while i%period != target%period:
        i -= 1
    return record[i]
    



grid = []
for line in f:
    line = line.rstrip()
    gLine = []
    for i in range(len(line.rstrip())):
        gLine.append(line[i])
    grid.append(gLine)

grid = rollAll(grid, 1)
answerOne = load(grid)

grid = rollAll(grid, 2)
grid = rollAll(grid, 4)
grid = rollAll(grid, 3)

answerTwo = spin(grid, 11, 999999999)


print(answerOne)
print(answerTwo)
print (time.process_time())