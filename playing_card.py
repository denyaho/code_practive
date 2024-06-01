import random

class Card:
    def __init__(self,value,suit,intValue):
        self.value=value
        self.suit=suit
        self.intValue=intValue
    
    def getCardString(self):
        return self.suit+self.Value+"(" + str(self.intValue) + ")"

class Deck:
    def __init__(self):
        self.Deck=self.generateDeck()
    
    @staticmethod
    def generateDeck():
        newDeck=[]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["♣", "♦", "♥", "♠"]

        for suit in suits:
            for i,value in enumerate(values):
                newDeck.append(Card(value,suit,i+1))
        return newDeck
    
    def draw(self):
        return self.deck.pop()
    
    def printDeck(self):
        print("Displaying cards...")
        for card in self.deck:
            print(card.getCardString())
    
    def shuffleDeck(self):
        deckSize=len(self.deck)
        for i in range(deckSize-1,0,-1):
            j=random.randint(i,deckSize-1)
            temp=self.deck[i]
            self.deck[i]=self.deck[j]
            self.deck[j]=temp

class Dealer:

    @staticmethod
    def startGame(amountOfPlayers):
        table={
            "players": [],
            "deck": Deck()
        }
        table["deck"].shuffleDeck()
        for person in range(0,amountOfPlayers):
            playerCard=[]
            for i in range(0,2):
                playerCard.append(table["deck"].draw())
                table["players"].append(playerCard)
        return table["players"]

table1=Dealer.startGame(2)
for bi in range(0,2):
    print(table[0][i].getCardString())