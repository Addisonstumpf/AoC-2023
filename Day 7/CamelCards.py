def hand(inStr:str, useJokers:bool=False)->int:
    counts = [0,0,0,0,0]
    for i in range(len(inStr)):
        if inStr[i]!='J' or not useJokers:
            counts[inStr.count(inStr[i])-1]+=1
    jokers = 5-sum(counts)
    if jokers == 5:
        return 7
    while jokers>0:
        i=3
        while counts[i]==0:
            i-=1
        counts[i]-=i+1
        counts[i+1]+=i+2
        jokers-=1
    if counts[4]==5:
        return 7
    elif counts[3]==4:
        return 6
    elif counts[2]==3:
        if counts[1]==2:
            return 5
        else:
            return 4
    elif counts[1]==4:
        return 3
    elif counts[1]==2:
        return 2
    else:
        return 1
    
cards = {'A':14, 'K':13, 'Q':12, 'J':1, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}  

def lesserHand(handOne, handTwo, useJokers:bool=True):
    answer = None
    if hand(handOne,useJokers)<hand(handTwo,useJokers):
        answer=True
    elif hand(handOne,useJokers)>hand(handTwo,useJokers):
        answer =False
    else:
        i=0
        while answer == None:
            if cards[handOne[i]]<cards[handTwo[i]]:
                answer = True
            elif cards[handOne[i]]>cards[handTwo[i]]:
                answer = False
            i+=1
    return answer
    


f = open(r"Day 7\input.txt","r")
#f = open(r"Day 7\sample.txt","r")

lines = []
answerOne = 0
answerTwo = 0

for line in f:
    lines.append([line[:5], int(line[5:])])

i=0
while i<len(lines)-1:
    if lesserHand(lines[i+1][0], lines[i][0]):
        lines[i+1], lines[i] = lines[i], lines[i+1]
        i=max(0, i-1)
    else:
        i+=1
print(lines)
i=0
while i<len(lines):
    answerOne+=(i+1)*lines[i][1]
    i+=1

print(answerOne)
print(answerTwo)