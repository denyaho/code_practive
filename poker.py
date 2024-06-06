def rankToValue(card):
    if card=="J":
        return 11
    if card=="Q":
        return 12
    if card=="K":
        return 13
    if card=="A":
        return 14
    return int(card)

def winnerPairOfCards(player1,player2):
    map_card1={}
    map_card2={}
    for i in range(len(player1)):
        map_card1[rankToValue(player1[i][1:])]=map_card1.get(rankToValue(player1[i][1:]),0)+1
        map_card2[rankToValue(player2[i][1:])]=map_card2.get(rankToValue(player2[i][1:]),0)+1
    
    sorted_card1=sorted(map_card1.items(),key=lambda x:(x[1],x[0]),reverse=True)
    sorted_card2=sorted(map_card2.items(),key=lambda x:(x[1],x[0]),reverse=True)

    print(sorted_card1)
    print(sorted_card2)
    for (value1,count1),(value2,count2) in zip(sorted_card1,sorted_card2):
        if count1>count2:
            return "player1"
        elif count1<count2:
            return "player2"
        elif value1>value2:
            return "player1"
        elif value1 < value2:
            return "player2"   
    if len(sorted_card1) > len(sorted_card2):
        return "player1"
    elif len(sorted_card2) > len(sorted_card1):
        return "player2" 
    return "draw"
