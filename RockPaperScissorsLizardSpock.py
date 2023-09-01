import random
def scoreRpsls(move1,move2):
    #all moves and results
    what={
        'rock':[{'scissors':'crushes'},{'lizard':'crushes'}],
        'paper':[{'rock':'covers'},{'spock':'disproves'}],
        'scissors':[{'paper':'cuts'},{'lizard':'decapitates'}],
        'lizard':[{'paper':'eats'},{'spock':'poisons'}],
        'spock':[{'rock':'vaporizes'},{'scissors':'smashes'}],
    }
    #if 1 is in 2 2 defeats 2 and so 
    if move1 in what[move2][0]:
        return "player2 wins \n"+move2 +" "+ what[move2][0][move1] +" "+ move1
    elif move2 in what[move1][0]:
        return "player1 wins \n"+move1 +" "+ what[move1][0][move2] +" "+ move2
def playRpsls():
    plays=['rock','paper','scissors','lizard','spock']
    #select 2 moves to play use  pop to stop repetion
    print(scoreRpsls(plays.pop(random.randint(0,4)),plays.pop(random.randint(0,3))))
playRpsls()
