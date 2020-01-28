import random


compChoices = ["rock", "paper", "scissors"]
score= {"wins":0,"losses":0,"draws":0}

def playRound():
    rand = random.randint(0,2)
    print(rand)
    user = input("rock paper or scissors?")
    comp = compChoices[rand]
    print(user, comp)
    if user == comp:
        score["draws"] += 1
        return "Its a draw"
    if user == "rock":
        if comp == "scissors":
            score["wins"] += 1
            return "You won that round!"
        if comp == "paper":
            score["losses"] += 1
            return "You lost that round"
    if user == "paper":
        if comp == "scissors":
            score["losses"] += 1
            return "You lost that round"
        if comp == "rock":
            score["wins"] += 1
            return "You won that round"
    if user == "scissors":
        if comp == "paper":
            score["wins"] += 1
            return "You won that round"
        if comp == "rock":
            score["losses"] += 1
            return "You lost that round"
    
def startMatch():
    numRounds = int(input("How many rounds do you wish to play?"))
    
    for i in range(numRounds):
        print(playRound())
        
    return score

game1 = startMatch()

print(game1)
