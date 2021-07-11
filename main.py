import random
import os
import logo

os.system('cls')
print(logo.logo[0])

#################################### 
### Initial data
####################################
nextround = True
gameover = False
# cards = [11]
# risks = [21]
cards = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
risks = [17, 18, 19, 20, 21]
players = {}
ingame = {}
roundnumber = 0
realplayerposition = ""

def startplayers():

    ### Filling the table with players
    players = {"dealer" : []}
    # print(players)
    for i in range(0, playercount):
        personname = "Player "+ str(i+1)
        players[personname] = []
        # print(players)

    ### Everyone is preparing for the game before first round
    for person in players.keys():
        ingame[person] = True
        # print(ingame)
    return players

def nextcard(person):

    # to do:
    # card choise posibility decrease after taking card from the deck
    nextcard = random.choice(cards)
    print(f"{person} draw {nextcard}")
    hand = players[person] 
    hand.append(nextcard)
    players[person] = hand

def checkcards(hand):

    ### Players score
    score = sum(hand)
    for card in hand:
        if (score > 21) and (11 in hand):
            score -= 10
            hand.remove(11)
            hand.append(1)    
    return (score)

def decidetodrawnextcard(hand, redline):

    ### Player decide to take next card
    if checkcards(hand) < random.choice(redline):
        return True
    else:
        return False

def wincheck():

    ### Search for winners at the end of the round
    score = {}
    winner = ""
    otherwinners = "" 
    multitopscore = False
    topscore = -1

    for person in players.keys():
        current = checkcards(players[person])
        if current <= 21:
            if current == topscore:
                multitopscore = True
                otherwinners += person
                otherwinners += ", "
            elif current > topscore:
                otherwinners = ""
                winner = person
                topscore = current
                multitopscore = False
    if topscore == -1:
        print("Everyone loose")
    elif multitopscore:
        print(f"No one win. {otherwinners[:-2]} and {winner} have the same score {topscore}")
    else:
        print(f"{winner} win this round with score {topscore}")

def nextroundcheck():

    ### Does anyone play in this round?
    playerskeepplaying = 0
    for person in ingame.keys():
        if ingame[person]:
            playerskeepplaying +=1
    if playerskeepplaying >= 1:
        return True
    else:
        return False

def askplayer (question, positiveanswer, negativeanswer):
    wronginput = True
    while wronginput:
        answer = input(question).lower()
        # print(answer)
        if answer == positiveanswer:
            wronginput = False
            return True
        elif answer == negativeanswer:
            wronginput = False
            return False


####################################
### Filling the table with players
####################################
playercount = int(input("Input number of players "))
realplayeringame = askplayer (question="Input Y for joining the table or N for watching the game:", positiveanswer="y", negativeanswer="n")
if realplayeringame:
    realplayerposition ="Player "+(input("Chose your place ot the table (1-{playercount})"))

####################################
### Game body ###
####################################
while not gameover:

    ### New game start
    players = startplayers()
    # print(players)
    # print(ingame)
    # input("")
    while nextround:
        roundnumber += 1
        nextcardagree= True

        for person in players.keys():
            # input("")
            if ingame[person] == True:
                ### Every player one-by-one decide to take next card
                ### prevention from taking unlimited number of cards by real person (disagree to loose)
                if realplayeringame and (person == realplayerposition) and (checkcards(players[person]) > 21):
                    nextcardagree = askplayer (question="Input Y for next card or H for hold:", positiveanswer="y", negativeanswer="h")
                else:
                    nextcardagree = decidetodrawnextcard(players[person], risks)

                
                if nextcardagree:
                    ### Addindg new card to players hand
                    nextcard(person)
                else:
                    ### Player hold the hand till the end of game
                    print(f"{person} holds")
                    ingame[person] = False
                    nextround = nextroundcheck()
                    # print(nextround)
                    # input("")
                    
        print(f"---End of round {roundnumber}---")

    ### Search for winners at the end of the round      
    wincheck()
    
    ### Players show their cards at the end of the current game
    print(players)

    ### User interrupt
    exitdecision = askplayer (question="Input N for the next game or E for exit :", positiveanswer="e", negativeanswer="n")
    if exitdecision:
        gameover = True
    else:
        nextround = True
        roundnumber = 0

    




  
