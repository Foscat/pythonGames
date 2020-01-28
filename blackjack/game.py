import random

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    # All objects have this method but it can be overridden to give
    # custom outputs
    def __repr__(self):
        return self.number + " of " + self.suit
        
suits = [ "Hearts", "Spades", "Diamonds", "Clubs" ]

values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

def generateDeck():
    deck = []
    for suit in suits:
        for value in values:
            newCard= Card(suit, value)
            deck.append(newCard)
    return deck
        
myDeck = generateDeck()

deltCards =[]

def dealCards(firstHand, currentHand):
    if firstHand:
        card1 = myDeck[random.randint(0,51)]
        print(1, card1)
        currentHand.append(card1)
        
        card2 = myDeck[random.randint(0,51)]
        if card2 not in currentHand:
            print(2, card2)
            currentHand.append(card2)
            return currentHand
        else:
            print(4, card2)
            dealCards(False, currentHand)
            return
    else:
        newCard = myDeck[random.randint(0,51)]
        print(5, newCard)
        if newCard not in currentHand:
            print(6, newCard)
            currentHand.append(newCard)
            return currentHand
        else:
            print(7, newCard)
            dealCards(False, currentHand)
            return
                
#dealCards(True, deltCards)
#dealCards(False, deltCards)
#print(deltCards)
              
#Gives a int value for each card            
def valueGiver(card):
    cv = card.number
    if cv == "Ace" or cv == "Jack" or cv == "Queen" or cv =="King":
        cv = 10
    else:
        cv = int(cv)
    return cv

#Takes a current hand and checks its total value
def checkHand(hand):
    handValue=0
    for index in hand:
        handValue += valueGiver(index)
    return handValue

#cHand = checkHand(deltCards)
#print(cHand)

def checkWinner(p,d):
    if p > 21:
        print("Aww you busted")
        if d > 21:
            print("and so did the dealer")
            return "None"
        else:
            print("The house always wins")
            return "Dealer"
    else:
        if d > 21:
            print("Th dealer buster and you didn't good job")
            return "Player"
        if p == 21:
            if d == 21:
                print("You and the dealer both hit 21!")
                return "Tie"
            else:
                print("Winner winner chicken dinner!")
                return "Player"
        elif d == 21:
            print("The house just won")
            return "Dealer"
        elif p > d:
            print("You got a higher score than the dealer!")
            return "Player"
        elif p < d:
            print("The dealer had a higher score. You lose.")
            return "Dealer"

def playGame(firstRound, playerHand, dealerHand):
    if firstRound:
        play = input("Want to play a had of blackjack? y/n")
        if play == "n":
            print("Well ok then, bye")
            return
        if play == "y":
            print("May the odds be ever in your favor")
            
            playerHand = dealCards(True, playerHand)
            dealerHand = dealCards(True, dealerHand)
            print("Player cards", playerHand)
            print("Dealer cards", dealerHand)
            
            ph = checkHand(playerHand)
            dh = checkHand(dealerHand)
            print("Player:"+str(ph), "Dealer:"+str(dh))
            
            if ph >= 21 or dh >= 21:
                return checkWinner(ph,dh)
            else:
                hs = input("Hit or stay? h/s")
                if hs == "h":
                    return playGame(False, playerHand, dealerHand)
                else:
                    return checkWinner(ph,dh)
                
        else:
            print("Use y or n for your answer")
            playGame(True, [], [])
    else:
        playerHand = dealCards(False, playerHand)
        
        ph = checkHand(playerHand)
        dh = checkHand(dealerHand)
        
        if dh < 17:
            dealerHand = dealCards(False, dealerHand)
        
        if ph >= 21 or dh >= 21:
            print("Player:"+str(ph), "Dealer:"+str(dh))
            return checkWinner(ph,dh)
        else:
            hs = ("Hit or stay? h/s")
            if hs == "h":
                return playGame(False, playerHand, dealerHand)
            else:
                print("Player:"+str(ph), "Dealer:"+str(dh))
                return checkWinner(ph,dh)
        
        
        
game1 = playGame(True, [], [])
print(game1)