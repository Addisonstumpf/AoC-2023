
def parseLine(iStr):
    while not (iStr[0].isnumeric() or iStr.startswith(("one", "two","three", "four", "five", "six", "seven", "eight", "nine", "zero"))):
        iStr = iStr[1:]

    if iStr[0].isnumeric():
        intrm = int(iStr[0])
    elif iStr.startswith("one"):
        intrm = 1
    elif iStr.startswith("two"):
        intrm = 2
    elif iStr.startswith("three"):
        intrm = 3
    elif iStr.startswith("four"):
        intrm = 4        
    elif iStr.startswith("five"):
        intrm = 5
    elif iStr.startswith("six"):
        intrm = 6
    elif iStr.startswith("seven"):
        intrm = 7
    elif iStr.startswith("eight"):
        intrm = 8
    elif iStr.startswith("nine"):
        intrm = 9
    elif iStr.startswith("zero"):
        intrm = 0

    result = intrm*10

    while not (iStr[-1].isnumeric() or iStr.endswith(("one", "two","three", "four", "five", "six", "seven", "eight", "nine", "zero"))):
        iStr = iStr[:len(iStr)-1]

    if iStr[-1].isnumeric():
        intrm = int(iStr[-1])
    elif iStr.endswith("one"):
        intrm = 1
    elif iStr.endswith("two"):
        intrm = 2
    elif iStr.endswith("three"):
        intrm = 3
    elif iStr.endswith("four"):
        intrm = 4        
    elif iStr.endswith("five"):
        intrm = 5
    elif iStr.endswith("six"):
        intrm = 6
    elif iStr.endswith("seven"):
        intrm = 7
    elif iStr.endswith("eight"):
        intrm = 8
    elif iStr.endswith("nine"):
        intrm = 9
    elif iStr.endswith("zero"):
        intrm = 0

    result = result+intrm
    return(result)
f = open("input.txt","r")
#f = open("sample.txt","r")

lines = []
i = 0
answer = 0
#print(parseLine("test123test"))

for line in f:
   answer=answer+parseLine(line)

print(answer)
