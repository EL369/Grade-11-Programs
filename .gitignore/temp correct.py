## Declare all variables

messagelist = ["Enter the Temperature type", "Invalid temperature TYPE should be C or F", "Enter the temperature to be converted", "Temperature is out of range", "Enter q to quit"]

Intemp = 212

Tempout = 0

validchoice = ["C", "c", "F", "f"]

keepgoing = True

Temptype = "F"

def getvalidtemptype( whichmessage, validinput ):

    global messagelist

    Temptype = input (messagelist [whichmessage])

    while not (Temptype in validinput):

     print (messagelist [whichmessage+1])

     Temptype = input (messagelist [whichmessage])

    return (Temptype)

## Start a loop (repeat until)

while keepgoing:

## Get a temperature

## Temperature could be wrong (range: -40 - 140)

## Could be non-numeric

## Invalid input

## Function called get valid temperature

## Celsius or Fahrenheit

## C for Celsius and F for Fahrenheit

## Force them to enter C or F

    Temptype = getvalidtemptype (0, validchoice)

## Calculations

## if statement

    if Temptype == "C":

      Tempout = Intemp * 9/5 + 32

    else:

        Tempout = (Intemp - 32) * 5/9

    print ("Your temperature is:", Tempout)

## print out the results

## Check to see if program is over

    keepgoing = not ("q" == input ("Enter q to quit"))

## Use an ask routine