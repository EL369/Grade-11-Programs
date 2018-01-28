## Neme: Evelyn Li
## Date: May, 1st
## Date last revised: May, 15th

## Purpose:
## Two players card game. Start with user against computer.
## Two cards are dealt, the player is asked if want to bet, the intent is to guess
## If bet, ask for how much player wants to bet
##     if the random generated 3rd card is between first two cards, player gets that much money, dealer loses that money
##     if not, the player loses money, dealer gets money

## Exception: if there is one Ace: player chooses if it's 1 or 14
##            if there are two Aces, automatically one high and one low.

## The Game Finishes: -when the player runs out of money
##                    -when the pot runs out of money
##                    -when the player quits
##                    -when there're not enough cards

## Thinking: - Create a 2D list for 2 cards, sort them with bubble sort
##          - Create an extra list for 3rd card, compare to see if it's between 1st and 2nd
##              Or add the 3rd card into the same list for 1st 2nd then sort them
##          - All the list variables should be local, call function using global var




## Variable Map

## NAME                              PUPOSE                                    TYPE                       RANGE
## deckGlobal                        hold the deck of cards                    2D arrray (4*13)            N/A
## cardchoice                        hold the random generated cards           2D array  (2*2)             N/A
## newcard                           hold the 3rd card                         list                        N/A
## suitval                           hold the suit value                       int                         0-3
## cardval                           hold the card value                       int                         0-12
## cardcountGlobal                   hold the number of the total cards left   int                         0-52
## initbank                          the initial bank balance                  int                         1000
## bankbalance                       hold the balance of the bank              int                         0-1000
## initmoney                         the initial money player has              int                         1000
## money                             hold the balance of user                  int                         0-2000
## bet                               hold the $ of each bet                    int                         N/A



## Declare Variables

card= ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "J", "Q", "K"]
suit= ["Club", "Diamond", "Heart", "Spade"]
deckGlobal= []
cardchoice= []
newcard= []
validchoice= []

suitval=0
cardval=0
cardcountGlobal=0

initbank = 1000
bankbalance = initbank

initmoney= 1000
money= initmoney

keepgoing= True
bet=0


import random


## Functions

## Initialize Deck
def initdeck (deck, numsuit, numcard, cardcount):
    cardcount = numsuit * numcard
    deck = [[True] * numcard for i in range (numsuit)]
    return (deck, cardcount)



## Get as many cards as the game required
def getCards (deck, cardnum, list1, cardcount):
    list1= [[0]*2 for j in range(cardnum)]
    for i in range (cardnum):
        suitval= random.randint(0,3)
        cardval= random.randint(0,12)

        while deck[suitval][cardval]== False:
            suitval= random.randint(0,3)
            cardval= random.randint(0,12)


        print("Your", i+1, "card is", suit[suitval],card[cardval])
        list1[i]= [suitval, cardval]
        deck[suitval][cardval]= False

    cardcount= cardcount-cardnum
    list1= bubblesort (list1, cardnum)
    return (deck, cardcount, list1)


## Sort the list into numerical order
def bubblesort (list, limit):
    for i in range (1, limit):
        swap = False
        for j in range (0, limit-i):
            if list [j][1]> list [j+1][1]:
                list[j], list [j+1]= list [j+1], list[j]
            if  list [j][1]< list [j+1][1]:
                swap = True
        if not swap:
            break
    return list



## Get 1 card
def getOneCard (deck, list2, count):
    list2= [[0]*2 for j in range(1)]
    suitval= random.randint(0,3)
    cardval= random.randint(0,12)

    while deck[suitval][cardval]== False:
            suitval= random.randint(0,3)
            cardval= random.randint(0,12)

    print("Your 3rd card is", suit[suitval],card[cardval])
    list2=[suitval, cardval]
    deck[suitval][cardval]= False
    count= count-1
    return (deck, count, list2)


## Ask for response
validchoice = ["Y", "N"]

def response (validchoice, question):
    global keepgoing
    answer = (input (question).upper())[0] # take the 1st letter
    while answer not in validchoice:
        answer= (input ("Invalid input, try again:").upper())[0]

    return(answer == validchoice[0])


## 1. If get 1 Ace, user decide if it's valued 1 or 14
## 2. If get 2 Aces, one is 1 and other is 14
def Ace(newlist):
    validinput = ["h", "l"]
    if newlist[0][1]==0 and newlist[1][1]==0:
        newlist[1][1]=13

    elif newlist[0][1]==0:
        answer=(input("Do you want Ace to be high or low?"))[0]
        while answer not in validinput:
            print("Invalid input")
            answer=(input("Do you want Ace to be high or low?"))[0]
        if answer == "high":
            newlist[0][1]=13
            bubblesort(newlist, 2)
        elif answer == "low":
            newlist[0][1]==0

    return (newlist)



## Initialize the deck
deckGlobal, cardcountGlobal = initdeck (deckGlobal, 4, 13, cardcountGlobal)


while keepgoing:
## Get 2 cards
    print("You got:")
    deckGlobal,cardcountGlobal, cardchoice = getCards (deckGlobal, 2, cardchoice, cardcountGlobal)
    cardchoice = Ace(cardchoice)
## How much they want to bet
    bet = int(input("How much do you want to bet?"))
## If user enter 0, they can get another 2 cards, but loses money
    if bet == 0:
        money = money-10
        bankbalance = bankbalance+10
        print ("You lost $10 to change cards")
        keepgoing = True

    else:
## If they want to bet, get the 3rd card
        deckGlobal, cardcountGlobal,newcard = getOneCard(deckGlobal, newcard, cardcountGlobal)
## If the 3rd card value is between 1st and 2nd card, player wins money, dealer loses money
        if cardchoice[0][1] < newcard[1] and newcard[1] < cardchoice[1][1]:
            money = money + bet
            bankbalance = bankbalance- bet
            print ("You won money.")
## If the 3rd card value is not between 1st and 2nd card, player loses money, dealer wins money
        elif not(cardchoice[0][1] < newcard[1] and newcard[1] < cardchoice[1][1]):
            money = money - bet
            bankbalance = bankbalance + bet
            print ("You lost money.")

        print ("Your money left is:", money)
        print ("Bank balance:", bankbalance)
## The game stops if player runs out of money
        if money <= 0 :
            keepgoing = False
            print("You went bankrupt.")
## The game stops if dealer runs out of money
        elif bankbalance <= 0 :
            keepgoing = False
            print ("You won the game, congratulations!")
## The game stops if run out of cards
        elif cardcountGlobal < 3 :
            keepgoing = False
            print ("Ran out of cards.")
            if money > bankbalance:
                print ("You won the game, congratulations!")
            elif money < bankbalance:
                print ("You lost.")
            else:
                print ("Tie!")
            deckGlobal, cardcountGlobal = initdeck (deckGlobal, 4, 13, cardcountGlobal)
            keepgoing= (response(validchoice, "Do you want to play again? (Y or N)"))
## The game stops if player quits
        else:
            keepgoing= (response(validchoice, "Do you want to continue? (Y or N)"))



