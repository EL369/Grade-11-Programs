# R-P  0-1   -1   lose
# R-S  0-2   -2   Win
# P-R  1-0   1    Win
# P-S  1-2   -1   Lose
# S-P  2-1   1    Win
# S-R  2-0   2    lose

#            0    Same
#           -2,1  Win
#           -1,2  Lose

#Rock = 0, Paper = 1, Scissors = 2

##VARIABLE MAP
##NAME                              PUPOSE                              TYPE                       RANGE
##computer                 The random number computer chose             int                        0-2
##player                   The player's input                           string                     ""
##playernum                Convert player's input into num              int                        0-2
##wincount                 Num of times won                             int                        0-2
##losecount                num of times lost                            int                        0-2


##Declear variables
computer = 0
player = ""
playernum = 0
wincount = 0
losecount = 0
keepgoing = True

##Make a list of choices
validchoice = ["Rock", "Paper", "Scissors"]

##Define function
def getvalidinput( inval ):
    inval = input ("Please enter Rock, Paper, or Scissors:")
    while not (inval in validchoice):
        inval = input ("Invalid input, try again")
    return (inval)

##Computer chooses a random number, representing rock paper scissors
##Player input a valid choice
##Convert player's choice into a number
##Divide the two nums and print the result accd to their difference
##Break the loop when a person wins
while keepgoing:
    player = getvalidinput (player)
    playernum = validchoice.index(player)

    import random
    computer = random.randint(0,2)

    num = playernum - computer

    if num == -2 or num == 1:
        print ("You win")
        wincount = wincount +1
        if wincount >= 2:
            print("You won the game!")
            keepgoing = False
    elif num == -1 or num == 2:
        print ("You lose")
        losecount = losecount + 1
        if losecount >= 2:
            print("You lost the game!")
            keepgoing = False
    else:
        print ("Tie")





