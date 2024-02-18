import time

def hash(iStr) -> int:
    answer = 0
    for i in range(len(iStr)):
        answer += ord(iStr[i])* 17 ** (len(iStr)-i)
    answer = answer % 256
    return answer

f = open(r"Day 15\input.txt","r")
#f = open(r"Day 15\sample.txt","r")

lines = []
answerOne = 0
answerTwo = 0

for line in f:
    i=0
    done = False
    while not done:
        if i == len(line):
            lines.append(line[:i])
            done = True
        elif line[i] == ',':
            lines.append(line[:i])
            line = line[i+1:]
            i=0
        else:
            i += 1

lenses = {}
for line in lines:
    print (line, hash(line))
    answerOne += hash(line)
    i=0
    while line[i] != '=' and line [i] != '-':
        i += 1
    if line[i] == '=':
        lenses[line[:i]] = int(line[i+1:])
    else:
        try:
            del lenses[line[:i]]
        except:
            pass

boxes = []
for i in range(256):
    boxes.append(1)

for x, lens in enumerate(lenses):
    h = hash(lens)
    answerTwo += (1+h)*(lenses[lens])*boxes[h]
    boxes[h]+=1

print(answerOne)
print(answerTwo)
print (time.process_time())