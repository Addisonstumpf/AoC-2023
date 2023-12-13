import time
import functools
f = open(r"Day 12\input.txt","r")
#f = open(r"Day 12\sample.txt","r")

lines = []
answerOne = 0
answerTwo = 0

# def validate(inStr:str, grouping,soFar:bool = False):
#     inStr = inStr + 'E'
#     g=0
#     i=0
#     while g<len(grouping) :
#         while inStr[i] != '#':
#             i += 1
#             if i == len(inStr):
#                 return soFar
#         if inStr[i:i+grouping[g]]==grouping[g]*'#' and inStr[i+grouping[g]] != '#':
#             i+= grouping[g]
#             g+=1
#         else:
#             inStr = inStr[:-1]
#             if len(inStr[i:i+grouping[g]]) != grouping[g] or inStr[i+grouping[g]-1]:
#                 return soFar
#             else:
#                 return False
#     if inStr.find('#', i) != -1:
#         return False
#     return True

# if grouping = [], check for #, return 1       ?
# remove end empties                            Collapse
# central overlap                               Collapse, with ? end
# edge                                          Collapse
# non-fit                                       Collapse, with ? end

def groupLen(grouping):
    answer = sum(grouping)
    answer += len(grouping)-1
    return answer

#@functools.lru_cache()
def collapse(springs, grouping):
    ready = False
    while not ready:
        ready = True
        if grouping == []:
            pass
        while springs[0] == '.':
            del springs[0]
            if springs == []:
                return [0], [0]
        if len(springs) < groupLen(grouping):
            return [0], [0]
        if grouping == []:
            for i in range(len(springs)):
                if springs[i]=='#':
                    return [0],[0]
            return [],[]
        if springs == []:
            if grouping != []:
                return [0], [0]
        
        if springs[0] == '#':
            for i in range(grouping[0]):
                if springs[i] == '.':
                    return [0], [0]
            try:
                springs[grouping[0]] = springs[grouping[0]]
            except IndexError:
                return [], []
            if springs[grouping[0]] == '#':
                return [0], [0]
            del springs[:grouping[0]+1]
            del grouping[0]
            ready = False
        elif springs[0] == '?':
            freeLen = 0
            state = 0 
            onset = -1
            while state > -1:
                freeLen += 1
                if freeLen == len(springs):
                    if state == 1: 
                        state = -1
                    else:
                        state = -2
                elif onset > 0 and freeLen >= onset+grouping[0]:
                    if springs[freeLen] == '#':
                        springs[onset-1] = '#'
                        ready = False
                    state = -1                    
                elif springs[freeLen] == '.':
                    if state == 1: 
                        state = -1
                    else:
                        state = -2
                elif springs[freeLen] == '#':
                    if state == 0:
                        onset = freeLen
                    state = 1
                elif springs[freeLen] == '?':
                    if state == 1 :
                        if freeLen < grouping[0]:
                            springs[freeLen] = '#'
                            ready = False
            if freeLen<grouping[0]:
                if state == -1:
                    return [0],[0]
                else:
                    del springs[:freeLen]
                    ready = False
            elif freeLen < 2*grouping[0] and state == -1:
                onset = freeLen-grouping[0]
                overlap = freeLen-2*onset
                for i in range(overlap):
                    springs[onset+i] = '#'
        if grouping == []:
            for i in range(len(springs)):
                if springs[i]=='#':
                    return [0],[0]
            return [],[]
        if springs == []:
            if grouping != []:
                return [0], [0]    
    ready = False
    while not ready:
        ready = True
        while springs[-1] == '.':
            del springs[-1]
            if springs == []:
                return [0], [0]     
        if springs[-1] == '#':
            for i in range(grouping[-1]):
                if springs[-1-i] == '.':
                    return [0], [0]
            try:
                springs[-grouping[-1]-1] = springs[-grouping[-1]-1]
            except IndexError:
                return [], []
            if springs[-grouping[-1]-1] == '#':
                return [0], [0]
            del springs[-grouping[-1]-1:]
            del grouping[-1]
            ready = False
        elif springs[-1] == '?':
            freeLen = 0
            state = 0 
            onset = -1
            while state > -1:
                freeLen += 1
                if freeLen == len(springs):
                    if state == 1: 
                        state = -1
                    else:
                        state = -2
                elif onset > 0 and freeLen >= onset+grouping[-1]:
                    if springs[-1-freeLen] == '#':
                        springs[-1-(onset-1)] = '#'
                        ready = False
                    state = -1                    
                elif springs[-1-freeLen] == '.':
                    if state == 1: 
                        state = -1
                    else:
                        state = -2
                elif springs[-1-freeLen] == '#':
                    if state == 0:
                        onset = freeLen
                        state = 1
                elif springs[-1-freeLen] == '?':
                    if state == 1 :
                        if freeLen < grouping[0]:
                            springs[-1-freeLen] = '#'
                            ready = False
            if freeLen<grouping[0]:
                if state == -1:
                    return [0],[0]
                else:
                    del springs[-1-freeLen:]
                    ready = False
            elif freeLen < 2*grouping[0] and state == -1:
                onset = freeLen-grouping[0]
                overlap = freeLen-2*onset
                for i in range(overlap):
                    springs[-1-(onset+i)] = '#'
        if grouping == []:
            for i in range(len(springs)):
                if springs[i]=='#':
                    return [0],[0]
            return [],[]
        if springs == []:
            if grouping != []:
                return [0], [0]    
    return springs, grouping

def possibility(springs:list, grouping):
    springs, grouping = collapse(springs, grouping)
    if grouping == [] and springs == []:
        return 1
    if springs[0] == 0:
        return 0
    springs[0] = '.'
    springs[-1] = '.'
    oSprings = springs.copy()
    oGroup = grouping.copy()
    answer = possibility(springs, grouping)
    springs = oSprings.copy()
    grouping = oGroup.copy()
    springs[-1] = '#'
    answer += possibility(springs, grouping)
    springs = oSprings.copy()
    grouping = oGroup.copy()
    springs[0] = '#'
    answer += possibility(springs, grouping)
    springs = oSprings.copy()
    grouping = oGroup.copy()
    springs[0] = '#'
    springs[-1] = '#'
    answer += possibility(springs, grouping)
    return answer


for x,line in enumerate(f):
    inStr, grouping = line.rstrip().split(' ')
    springs = []
    for i in range(len(inStr)):
        springs.append(inStr[i])

    grouping = list(map(int, grouping.split(',')))
    answer= possibility(springs, grouping)
    print (x, line, answer)
    answerOne += answer
    inStr, grouping = line.rstrip().split(' ')
    springs = []
    for i in range(len(inStr)):
        springs.append(inStr[i])
    grouping = list(map(int, grouping.split(',')))
    grouping = 5*grouping
    springs.append('?')
    springs = springs*5
    del springs[-1:]
    # inStr = inStr + '?' + inStr + '?' + inStr + '?' + inStr + '?' + inStr
    answerTwo += possibility(springs, grouping)

    print(x+1)

print(answerOne)
print(answerTwo)
print (time.process_time())