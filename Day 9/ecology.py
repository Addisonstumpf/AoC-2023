import time
f = open(r"Day 9\input.txt","r")
#f = open(r"Day 9\sample.txt","r")

answerOne = 0
answerTwo = 0

def extrapolate(line, back:bool=False)->int:
    deeper = []
    bottom=True
    for i in range(len(line)-1):
        deeper.append(line[i+1]-line[i])
        if line[i+1]-line[i] and bottom:
            bottom=False
    if bottom:
        return line[0]
    else:
        if back:
            answer = line[0]-extrapolate(deeper, True)
        else:
            answer = line[len(line)-1]+extrapolate(deeper)
    return answer
    
for item in f:
    line=list(map(int, item.rstrip().split(' ')))
    answerOne+=extrapolate(line)
    answerTwo+=extrapolate(line, True)

print(answerOne)
print(answerTwo)
print (time.process_time())