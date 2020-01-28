class Player:
    '''
    For use with Black-Jack game to create player
    '''
    def __init__(self, name):
        self.name = name
        self.bank = 1000 # new player init at $1000
        self.rounds = 0  # new player init at 0
        self.bet = 0 # new player init at 0
        self.cards = []
        self.numberOfCards = 0
        
    def hand(self, card):
        self.cards.append(card)
        self.numberOfCards = len(self.cards)
        max = self.numberOfCards
        self.val = 0
        aceCount = 0
                
        for i in range(0, max):
            if 'Ace' in self.cards[i]:
                self.val = self.val + 11
                aceCount = 1

            if 'King' in self.cards[i]:
                self.val = self.val + 10

            if 'Queen' in self.cards[i]:
                self.val = self.val + 10

            if 'Jack' in self.cards[i]:
                self.val = self.val + 10

            if '10 of' in self.cards[i]:
                self.val = self.val + 10

            if '9 of' in self.cards[i]:
                self.val = self.val + 9

            if '8 of' in self.cards[i]:
                self.val = self.val + 8

            if '7 of' in self.cards[i]:
                self.val = self.val + 7

            if '6 of' in self.cards[i]:
                self.val = self.val + 6

            if '5 of' in self.cards[i]:
                self.val = self.val + 5

            if '4 of' in self.cards[i]:
                self.val = self.val + 4

            if '3 of' in self.cards[i]:
                self.val = self.val + 3

            if '2 of' in self.cards[i]:
                self.val = self.val + 2

        if (aceCount >= 1) and (self.val > 21):
            self.val = self.val - 10
        if (aceCount >= 2) and (self.val > 21):
            self.val = self.val - 10
        if (aceCount >= 3) and (self.val > 21):
            self.val = self.val - 10
        if (aceCount >= 4) and (self.val > 21):
            self.val = self.val - 10
        if (aceCount >= 5) and (self.val > 21):
            self.val = self.val - 10

        return(self.val)

    def printCards(self):
        for i in self.cards:
            print(i)

class DeckOfCards:
    '''
    This object provides a dictionary of playing cards
    
        :parameter num:  integer that sets the number of decks to be constructed
        :parameter joker:  boolean that where True include the Joker card and False it no Joker card
        :return: dictionary with an integer as a key and string representing the playing card description
        
    '''
    def __init__(self, num=1, joker=False):
        self.num = num * 52  #number of decks to be constructed
        self.joker = joker
        self.playingCards = {0: 'Joker', 1: 'Ace of Spades', 2: 'King of Spades', 3: 'Queen of Spades', 4: 'Jack of Spades', 
                         5: '10 of Spades', 6: '9 of Spades', 7: '8 of Spades', 8: '7 of Spades',
                         9: '6 of Spades', 10: '5 of Spades', 11: '4 of Spades', 12: '3 of Spades',
                         13: '2 of Spades',
                         14: 'Ace of Hearts', 15: 'King of Hearts', 16: 'Queen of Hearts', 17: 'Jack of Hearts',
                         18: '10 of Hearts', 19: '9 of Hearts', 20: '8 of Hearts', 21: '7 of Hearts',
                         22: '6 of Hearts', 23: '5 of Hearts', 24: '4 of Hearts', 25: '3 of Hearts',
                         26: '2 of Hearts',
                         27: 'Ace of Clubs', 28: 'King of Clubs', 29: 'Queen of Clubs', 30: 'Jack of Clubs',
                         31: '10 of Clubs', 32: '9 of Clubs', 33: '8 of Clubs', 34: '7 of Clubs',
                         35: '6 of Clubs', 36: '5 of Clubs', 37: '4 of Clubs', 38: '3 of Clubs',
                         39: '2 of Clubs',
                         40: 'Ace of Diamonds', 41: 'King of Diamonds', 42: 'Queen of Diamonds', 43: 'Jack of Diamonds',
                         44: '10 of Diamonds', 45: '9 of Diamonds', 46: '8 of Diamonds', 47: '7 of Diamonds',
                         48: '6 of Diamonds', 49: '5 of Diamonds', 50: '4 of Diamonds', 51: '3 of Diamonds',
                         52: '2 of Diamonds'}
       
        if self.joker == True:
            cardIndexing = 0
        else:
            cardIndexing = 1
    
    # building multi-decks
        if self.num > 1:
            cardIndexing
            for n in range(53, self.num):
                self.playingCards[n] = self.playingCards[cardIndexing]
                if cardIndexing == 52:
                    if self.joker == True:
                        cardIndexing = 0
                    else:
                        cardIndexing = 1
                else:
                    cardIndexing += 1

def clearScreen():
    for i in range(1,30):
        print(i * '>')
    i = 30
    while i != 0:
        print(i * '<')
        i -= 1

#==========================================
# Initilize of Game
#==========================================
import random
cardsInRandom = list(range(1,312))
cardAtTopOfDeck = 0
playerHit = True
dealerHit = True
playOkay = True
betOkay = False
random.shuffle(cardsInRandom)
# later I'm going to allow multi-players ect. here
playerNo1 = Player('A. Player')
dealer = Player('Dealer')
deck = DeckOfCards(6)
clearScreen()

# ===========================================================================================
#  Game Start.  Dealing out the cards to player and dealer
# ===========================================================================================
while playOkay == True:

    print('You have $' + str(playerNo1.bank) + ' in your bank account' + '\n')
    betOkay = False

    while betOkay == False:
        playerNo1.bet = input('Place your bet: $')
        if int(playerNo1.bet) > playerNo1.bank:
            print('That\'s more than you have in the bank')
            betOkay = False
        else:
            betOkay = True
            clearScreen()
            
    # Dealing out inital round of cards
    # later add muti-players here and build a loop to
    # deal out the cards
    playerNo1.hand(deck.playingCards[cardsInRandom[cardAtTopOfDeck]])
    cardAtTopOfDeck += 1
    
    dealer.hand(deck.playingCards[cardsInRandom[cardAtTopOfDeck]])
    cardAtTopOfDeck += 1

    playerNo1.hand(deck.playingCards[cardsInRandom[cardAtTopOfDeck]])
    cardAtTopOfDeck += 1
    
    dealer.hand(deck.playingCards[cardsInRandom[cardAtTopOfDeck]])
    cardAtTopOfDeck += 1
    

    print('----- Your hand -----')
    playerNo1.printCards()
    print(30 * '=' + '\n')

    print('Your hand\'s value:  ' + str(playerNo1.val))
    print('your bet is: $' + str(playerNo1.bet) + '\n')
    print(30 * '=' + '\n')

    print('----- Dealer\'s top card showing -----')
    print(dealer.cards[0])
    print(30 * '=' + '\n')

    playerHit = True
    dealerHit = True

    # ===========================================================================================
    #  Stage2, player is prompted to HIT or STAY then re-cal player's hand
    #  if the player stays or completes his HITs the dealer draws cards until reaching >= 17
    # ===========================================================================================
    while playerHit == True:
        myHand_HitStay = input('Enter: \"H\" for Hit or \"S\" for Stay  ')
        myHand_HitStay = myHand_HitStay.lower()

        if 'h' in myHand_HitStay:
            playerHit = True
            playerNo1.hand(deck.playingCards[cardsInRandom[cardAtTopOfDeck]])
            cardAtTopOfDeck += 1
            clearScreen()
            print('----- Your hand -----')
            playerNo1.printCards()
            print(30 * '=' + '\n')
            print('Your hand\'s value:  ' + str(playerNo1.val) + '\n')
            print('your bet is: ' + str(playerNo1.bet) + '\n')
            print(30 * '=' + '\n')
            print('----- Dealer\'s top card showing -----')
            print(dealer.cards[0])
            print(30 * '=' + '\n')
        else:
            playerHit = False

        if playerNo1.val > 21:
            clearScreen()
            playerHit = False
            print(30 * '=')
            print('Player BUST ...')
            print(30 * '=' + '\n')
            dealerHit = False



    while dealerHit == True:
        if dealer.val < 17:
            dealer.hand(deck.playingCards[cardsInRandom[cardAtTopOfDeck]])
            cardAtTopOfDeck += 1
        else:
            dealerHit = False


    if dealer.val > 21:
        print(30 * '=')
        print('Dealer BUST ...')
        print(30 * '=' + '\n')

    # ===========================================================================================
    #  Show Results
    # ===========================================================================================
    print(30 * '=' + '\n')
    print('----- Your hand -----')
    playerNo1.printCards()
    print(30 * '=' + '\n')
    print('Your hand\'s value:  ' + str(playerNo1.val))

    print('----- Dealer\'s hand -----')
    dealer.printCards()
    print(30 * '=' + '\n')
    print('Dealer\'s hand value:  ' + str(dealer.val))
    

    if ((playerNo1.val <= 21) and (playerNo1.val >= dealer.val)) or (dealer.val > 21):
        print(30 * '=' + '\n')
        print('Player Wins')
        print(30 * '=' + '\n')
        playerNo1.bank = playerNo1.bank + int(playerNo1.bet)
        dealer.bank = dealer.bank - int(playerNo1.bet)
        
    else:
        print(30 * '=' + '\n')
        print('Dealer Wins')
        print(30 * '=' + '\n')
        playerNo1.bank = playerNo1.bank - int(playerNo1.bet)
        dealer.bank = dealer.bank + int(playerNo1.bet)

    print('Player\'s Bank Account: $'+ str(playerNo1.bank))
    print('Dealer\'s Bank Account: $'+ str(dealer.bank))

    if playerNo1.bank <= 0:
        print('Sorry your out of money.  GAME OVER!  Better luck next time!')
        break

    if dealer.bank <= 0:
        print('House is out of money.  PLAYER WINS!!!')
        break

    print('Play Again?' + '\n')
    playOn = input('Enter: \"Y\" for Yes or \"N\" for No  ')
    if 'y' in playOn:
        playOkay = True
        clearScreen()
        print('New Hand')
        print(30 * '=' + '\n')
        dealer.cards = []
        playerNo1.cards = []
    else:
        playOkay = False
        clearScreen()
        print('Your ending bank balance is:  ' + str(playerNo1.bank))


