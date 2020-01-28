import random

def rollOne():
    return random.randint(1,6)

def sum(a,b):
    return a+b

def rollDice():
    return sum(rollOne(),rollOne())

def playGame():
    
    firstRoll = rollDice()
    print("The first roll is "+str(firstRoll))
    
    if firstRoll == 7:
        return "Lucky number 7! You won on the first roll!"
    if firstRoll == 11:
        return "Heyy you got 11! Your won on the first roll!"
    if firstRoll == 2:
        return "Aww you rolled a 2. You lost on the first roll.."
    if firstRoll == 3:
        return "Three is no good around here. You lost on the first roll.."
    if firstRoll == 12:
        return "Double sixes huh? You lost on the first roll.."
    else:
        point = firstRoll
        hitPoint = True
        print("The point is " + str(point))
        
        newRoll = rollDice()
        print("Your next rolls is " + str(newRoll))
        
        if newRoll == point:
            return "Right on point. You win!"
        if newRoll == 7:
            return "Seven is no good on your second roll. You lose"
        else:
            while hitPoint:
                loopRoll = rollDice()
                print("New roll is " + str(loopRoll))
                
                if loopRoll == point:
                    hitPoint = False
                    return "You hit the point! You won!"
                if loopRoll == 7:
                    hitPoint = False
                    return "You hit a 7! You lose bucco!"
                
                
game1 = playGame()

print(game1)