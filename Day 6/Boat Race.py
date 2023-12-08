f = open(r"Day 6\input.txt","r")
#f = open(r"Day 6\sample.txt","r")

def firstWord(iStr: str) -> (str, str):
    answer = ''
    while iStr.startswith(' '):
        iStr=iStr[1:]
    while not iStr.startswith(' '):
        answer += iStr[:1]
        iStr= iStr[1:]
        if not iStr:
            break
    return answer, iStr

def waysToWin(time:int, dist:int)->int:
    answer = 0
    i=0
    while i*(time-i)<=dist:
        i+=1
    answer = time-(2*i)+1
    return answer


lines = []
bigTime = ''
bigDist = ''

answerOne = 1
answerTwo = 0

for line in f:
    lines.append(line)
time, times = firstWord(lines[0])
dist, dists = firstWord(lines[1])

for x in range(4):
    time, times = firstWord(times)
    dist, dists = firstWord(dists)
    bigTime+=time
    bigDist+=dist
    answerOne *=waysToWin(int(time),int(dist))

answerTwo = waysToWin(int(bigTime), int(bigDist))


print(answerOne)
print(answerTwo)