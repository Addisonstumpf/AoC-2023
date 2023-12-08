
f = open("input.txt","r")
#f = open("sample.txt","r")

lines = []
i = 0
answerOne = 0
answerTwo = 0

for line in f:
    workLine = []
    for i in range(len(line)):
        if line[i]!='\n':
            workLine.append(line[i])
    lines.append(workLine)
rowLen = len(lines[0])-1
colLen = len(lines)-1
#print (rowLen, colLen)

def includeNumber(lineNo, startNo, endNo) ->bool:
    debug = False
    if lineNo ==118 :
        #debug=True
        pass
    checkRows = []
    checkCols = []
    answer = False
    if debug:
        print(lineNo, startNo, endNo)
    if lineNo !=0:
        for j in range(max(0, startNo-1), min(endNo+1, rowLen)):
            checkRows.append(lineNo-1)
            checkCols.append(j)
    if startNo !=0:
        checkRows.append(lineNo)
        checkCols.append(startNo-1)
    if endNo <rowLen:
        checkRows.append(lineNo)
        checkCols.append(endNo)
    if lineNo <colLen:
        for j in range(max(0, startNo-1), min(endNo+1, rowLen)):
            checkRows.append(lineNo+1)
            checkCols.append(j)
    if debug==True:
        print(checkRows, checkCols)
    j=0
    while answer == False and  j <len(checkRows):
        if debug ==True:
            #print(checkRows[j], checkCols[j])
            pass
        if lines[checkRows[j]][checkCols[j]] != '.' and not lines[checkRows[j]][checkCols[j]].isnumeric():
            answer = True
        j +=1
    return answer
def numberAt(lineNo, colNo) ->int:
    answer = 0
    anStr = ''
    while lines[lineNo][colNo].isnumeric():
        anStr+=lines[lineNo][colNo]
        colNo+=1
        if colNo >rowLen:
            break
    answer = int(anStr)
    return answer
def gearRatio(lineNo, colNo) -> int:
    answer = 1
    countNo=0
    if lineNo!=0:
        if lines[lineNo-1][colNo].isnumeric():
            startNo=colNo
            while lines[lineNo-1][startNo].isnumeric():
                startNo-=1
                if startNo==-1:
                    break
            startNo+=1
            answer*=numberAt(lineNo-1, startNo)
            countNo+=1
        else:
            if lines[lineNo-1][max(0,colNo-1)].isnumeric():
                startNo=colNo-1
                while lines[lineNo-1][startNo].isnumeric():
                    startNo-=1
                    if startNo==-1:
                        break
                startNo+=1
                answer*=numberAt(lineNo-1, startNo)
                countNo+=1
            if lines[lineNo-1][min(rowLen, colNo+1)].isnumeric():
                answer*=numberAt(lineNo-1, colNo+1)
                countNo+=1
    if lineNo!=colLen:
        if lines[lineNo+1][colNo].isnumeric():
            startNo=colNo
            while lines[lineNo+1][startNo].isnumeric():
                startNo-=1
                if startNo==-1:
                    break
            startNo+=1
            answer*=numberAt(lineNo+1, startNo)
            countNo+=1
        else:
            if lines[lineNo+1][max(0,colNo-1)].isnumeric():
                startNo=colNo-1
                while lines[lineNo+1][startNo].isnumeric():
                    startNo-=1
                    if startNo==-1:
                        break
                startNo+=1
                answer*=numberAt(lineNo+1, startNo)
                countNo+=1
            if lines[lineNo+1][min(rowLen, colNo+1)].isnumeric():
                answer*=numberAt(lineNo+1, colNo+1)
                countNo+=1
    if lines[lineNo][max(0,colNo-1)].isnumeric():
        startNo=colNo-1
        while lines[lineNo][startNo].isnumeric():
            startNo-=1
            if startNo==-1:
                break
        startNo+=1
        answer*=numberAt(lineNo, startNo)
        countNo+=1
    if lines[lineNo][min(rowLen, colNo+1)].isnumeric():
        answer*=numberAt(lineNo, colNo+1)
        countNo+=1
    if countNo!=2:
        answer = 0
    return answer


workRow = 0
workCol = 0

while workRow <= colLen:
    workLen = 0
    workStr = ''
    if lines[workRow][workCol]=='*':
        answerTwo+=gearRatio(workRow, workCol)
    while lines[workRow][workCol+workLen].isnumeric()==True:
        workStr=workStr + lines[workRow][workCol+workLen]
        workLen+=1
        if workCol+workLen>rowLen:
            break
    if workLen == 0:
        workCol+=1
    else:
        #print('checking number', workStr, 'starting at', workRow, workCol, workLen)
        if includeNumber(workRow, workCol, workCol+workLen)==True:
            answerOne+=int(workStr)
        else:
            pass
            #print('rejected', workStr, workRow, workCol)
        workCol+=workLen
    #print (workCol, rowLen)
    if workCol >= rowLen:
        workCol = 0
        workRow+=1
        #print('starting row', workRow)

print(answerOne)
print(answerTwo)
