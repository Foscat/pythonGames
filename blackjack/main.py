# Create a Card class
class Card:
    # In python this is the constructor for the class. It needs the slef
    # as the first arg and acts similar to 'this' in other languages
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    # All objects have this method but it can be overridden to give
    # Custom outputs
    def __repr__(self):
        return self.number + " of " + self.suit
    # Define a getter for suit
    @property
    def suit(self):
        return sefl.suit
    # Define a setter for suit
    def suit(self, suit):
        if suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            self.suit = suit
        else:
            print("That is not a suit!")

# The __init__ function is called behind the scenes for  constructor
# No new keyword needed with constructors
myCard = Card("Spades", "10")

myCard.suit= "Hearts"

print(myCard)
