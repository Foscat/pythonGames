# ===========================================================================================
# Blackjack program start-up
# ===========================================================================================

import random

playingCards = {0: 'Joker',
                1: 'Ace of Spades', 2: 'King of Spades', 3: 'Queen of Spades', 4: 'Jack of Spades',
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

# ===========================================================================================
# builds the next 6 decks
# ===========================================================================================
cardIndexing = 1
for n in range(53, 365):
    playingCards[n] = playingCards[cardIndexing]
    if cardIndexing == 52:
        cardIndexing = 1
    else:
        cardIndexing += 1

# ===========================================================================================
# Initialize the program variables and shuffle the decks of cards
# ===========================================================================================

cardsInOrder = list(range(1,365))
cardsInRandom = list(range(1,365))
cardFromDeck = 0
playerHit = True
dealerHit = True
playOkay = True
betOkay = False
playerBank = 1000
dealerBank = 1000
random.shuffle(cardsInRandom)

# test to check that all the cards were built correctly
#for i in range(0,364):
#   print(str(i) + " : " + playingCards[cardsInOrder[i]])

def hand_value(a):
    """
    Blackjack game's hand value function

    :param a: input a list of strings that define the playing cards
    :return: integer value of the player's hand
    """

    aceCount = 0
    val=0
    max = len(a)

    for i in range(0, max):
        if 'Ace' in a[i]:
            val = val + 11
            aceCount = 1

        if 'King' in a[i]:
            val = val + 10

        if 'Queen' in a[i]:
            val = val + 10

        if 'Jack' in a[i]:
            val = val + 10

        if '10 of' in a[i]:
            val = val + 10

        if '9 of' in a[i]:
            val = val + 9

        if '8 of' in a[i]:
            val = val + 8

        if '7 of' in a[i]:
            val = val + 7

        if '6 of' in a[i]:
            val = val + 6

        if '5 of' in a[i]:
            val = val + 5

        if '4 of' in a[i]:
            val = val + 4

        if '3 of' in a[i]:
            val = val + 3

        if '2 of' in a[i]:
            val = val + 2

    if (aceCount >= 1) and (val > 21):
        val = val - 10
    if (aceCount >= 2) and (val > 21):
        val = val - 10
    if (aceCount >= 3) and (val > 21):
        val = val - 10
    if (aceCount >= 4) and (val > 21):
        val = val - 10
    if (aceCount >= 5) and (val > 21):
        val = val - 10

    return(val)

# ===========================================================================================
#  Game Start.  Dealing out the cards to player and dealer
# ===========================================================================================
while playOkay == True:

    print('You have $' + str(playerBank) + ' in your bank account' + '\n')
    betOkay = False

    while betOkay == False:
        playerBet = input('Place your bet: ')
        if int(playerBet) > playerBank:
            print('That\'s more than you have in the bank')
            betOkay = False
        else:
            betOkay = True

    myHand = [playingCards[cardsInRandom[cardFromDeck]], playingCards[cardsInRandom[cardFromDeck + 1]]]
    cardFromDeck = cardFromDeck + 2


    dealerHand = [playingCards[cardsInRandom[cardFromDeck]], playingCards[cardsInRandom[cardFromDeck + 1]]]
    cardFromDeck = cardFromDeck + 2


    myHandValue = hand_value(myHand)
    dealerHandValue = hand_value(dealerHand)


    print('Your hand:  ' + str(myHand))
    print('Your hand\'s value:  ' + str(myHandValue))
    print('your bet is: ' + str(playerBet) + '\n')

    print('Dealer\'s hand showing:  ' + str(dealerHand[0]))
    # print('Dealer\'s hand\'s value:  ' + str(dealerHandValue))
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
            myHand.append(playingCards[cardsInRandom[cardFromDeck]])
            cardFromDeck += 1
            myHandValue = hand_value(myHand)
            print('Your hand:  ' + str(myHand))
            print('Your hand\'s value:  ' + str(myHandValue) + '\n')
        else:
            playerHit = False

        if myHandValue > 21:
            playerHit = False
            print(30 * '=')
            print('BUST ...')
            dealerHit = False



    while dealerHit == True:
        if dealerHandValue < 17:
            dealerHand.append(playingCards[cardsInRandom[cardFromDeck]])
            cardFromDeck += 1
            dealerHandValue = hand_value(dealerHand)
        else:
            dealerHit = False


    if dealerHandValue > 21:
        print(30 * '=')
        print('BUST ...')

    # ===========================================================================================
    #  Show Results
    # ===========================================================================================
    print(30 * '=' + '\n')
    print('Your hand:  ' + str(myHand))
    print('Your hand\'s value:  ' + str(myHandValue) + '\n')

    print('Dealer\'s hand:  ' + str(dealerHand))
    print('Dealer\'s hand\'s value:  ' + str(dealerHandValue))
    print(30 * '=')

    if ((myHandValue <= 21) and (myHandValue >= dealerHandValue)) or (dealerHandValue > 21):
        print('Player Wins')
        print(30 * '=')
        playerBank = playerBank + int(playerBet)
        dealerBank = dealerBank - int(playerBet)
    else:
        print('Dealer Wins')
        print(30 * '=')
        playerBank = playerBank - int(playerBet)
        dealerBank = dealerBank + int(playerBet)

    print('Play Again?' + '\n')
    playOn = input('Enter: \"Y\" for Yes or \"N\" for No  ')
    if 'y' in playOn:
        playOkay = True
        print(30 * '=' + 5 * '\n')
        print(30 * '=' + '\n')
        print('New Hand')
        print(30 * '=' + '\n')
    else:
        playOkay = False
        print('Your ending bank balance is:  ' + str(playerBank))