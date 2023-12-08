def hand(inStr:str)->int:
    counts = [0,0,0,0,0]
    for i in range(len(inStr)):
        
        counts[inStr.count(inStr[i])-1]+=1
    print(counts)
    if sum(counts) !=5:
        print (counts)
        return ValueError
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
    
cards = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}  

def lesserHand(handOne, handTwo):
    answer = None
    #print(hand(handOne), hand(handTwo))
    if hand(handOne)<hand(handTwo):
        #print ('lose on hand', hand(handOne), hand(handTwo))
        answer=True
    elif hand(handOne)>hand(handTwo):
        #print ('win on hand', hand(handOne), hand(handTwo))
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

print(lesserHand("225JT", "235A4"))
