import time
f = open(r"Day 8\input.txt","r")
#f = open(r"Day 8\sample.txt","r")

def product(l):
    answer =1
    for i in l:
        answer *=i
    return answer
def progress(state, chunk, dir, deb:bool=False, startState='', step =0):
    loc = chunk.find('.'+state)+4
    if dir=='R':
        loc+=3
    answer = chunk[loc:loc+3]
    if deb and answer[2]=='Z':
        print(startState,answer,step)
    return answer

lines = []
answerOne = 0
answerTwo = 0
chunk = ''
directions=''
states = []
periodical = []
startStates = []

for line in f:
    if directions:
        if len(line)>5:
            chunk+='.'+line[0:3]+line[7:10]+line[12:15]
            if line[2]=='A':
                states.append(line[0:3])
                startStates.append(line[0:3])
                periodical.append(0)
    else:
        directions = line.rstrip()
    #do the thing

state = 'AAA'
i=0
while state !='ZZZ':
    state = progress(state,chunk,directions[i])
    i+=1
    if i==len(directions):
        i=0
    answerOne+=1
i=0
while product(periodical)==0:
    answerTwo+=1
    for j, substate in enumerate(states):
        states[j] = progress(substate,chunk,directions[i])
        if states[j][2]=='Z' and periodical[j]==0:
            periodical[j]=answerTwo
    i+=1
    if i==len(directions):
        i=0
        for j, substate in enumerate(states):
            if states[j] == startStates[j] and periodical[j]==0:
                periodical[j]=answerTwo/len(directions)

    # if answerTwo%50000==0:
    #     print(answerTwo, periodical)
def LCM(a:int, b:int)->int:
    if a==1:
        return b
    if b == 1:
        return a
    answer = a
    while answer%b != 0:
        answer +=a
    return answer
answerTwo = 1
for term in periodical:
    answerTwo = LCM(answerTwo, term)
print (periodical)
print(answerOne)
print(answerTwo)
print (time.process_time())