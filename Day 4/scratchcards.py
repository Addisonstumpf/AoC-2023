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
def winCard(ind:int, wins:int, cards:[int]) -> [int]:
    i=1
    mult = cards[ind]
    while i<=wins:
        cards[ind+i]+=cards[ind]
        i+=1
    return cards


f = open(r"Day 4\input.txt","r")
#f = open(r"Day 4\sample.txt","r")

lines = []
cards=[]
answerOne = 0
answerTwo = 0

for x in f:
    cards.append(1)
f.seek(0)
for x, line in enumerate(f):
    answerTwo+=cards[x]
    winners = line[line.find(':')+1:line.find('|')].rstrip()
    owned = ' ' + line[line.find('|')+1:].rstrip() + ' '
    exp= 0
    while winners:
        targ, winners = firstWord(winners)
        if targ and ' ' + targ + ' ' in owned:
            exp+=1
    if exp:
        answerOne+= (2**(exp-1))
        cards=winCard(x, exp, cards)
        
print (answerOne)
print (answerTwo)