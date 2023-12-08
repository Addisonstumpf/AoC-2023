
def possibleGame(iStr, red, blue, green):
    #print(iStr)
    result = True
    while len(iStr)>0 and result == True:
        i=0
        while iStr[i].isnumeric():
            i += 1
        cubeNo = int(iStr[:i])
        iStr = iStr[i+1:]
        if iStr.startswith("red"):
            if cubeNo > red:
                result = False
                #print(str(cubeNo) + " red greater than " + str(red))
            iStr = iStr[5:]
        elif iStr.startswith("blue"):
            if cubeNo >blue:
                result = False
                #print(str(cubeNo) + " blue greater than " + str(blue))
            iStr = iStr[6:]
        elif iStr.startswith("green"):
            if cubeNo > green:
                result = False
                #print(str(cubeNo) + " green greater than " + str(green))
            iStr = iStr[7:]
        else:
            print (iStr)
            raise ValueError
    return result
def gamePower(iStr):
    #print(iStr)
    red, blue, green = 0, 0, 0
    while len(iStr)>0:
        i=0
        while iStr[i].isnumeric():
            i += 1
        cubeNo = int(iStr[:i])
        iStr = iStr[i+1:]
        if iStr.startswith("red"):
            red = max(red, cubeNo)
            iStr = iStr[5:]
        elif iStr.startswith("blue"):
            blue = max(blue, cubeNo)
            iStr = iStr[6:]
        elif iStr.startswith("green"):
            green = max(green, cubeNo)
            iStr = iStr[7:]
        else:
            print (iStr)
            raise ValueError
    result = red * blue * green
    return result

f = open("input.txt","r")
#f = open("sample.txt","r")

lines = []
i = 0
answer = 0

for line in f:
    workLine = line[5:]
    i=0
    while workLine[i].isnumeric():
        i+=1
    gameNo = int(workLine[:i])
    workLine = workLine[i+2:]
    
    # if possibleGame(workLine, 12,14,13)==True:
    #     print ("adding " + str(gameNo))
    #     answer += gameNo
    # else:
    #     print ("not adding " + str(gameNo))
    answer += gamePower(workLine)

print(answer)

    
