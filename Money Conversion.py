##                          Variable Map
##  NAME          PURPOSE                         TYPE                       RESTRICTIONS
## penny        # of pennies                      int                         0 to 1000
## highval      max # of penny                     int                              0
## lowval       min # of penny                      int                         1000

highval= 1000
lowval=0
penny=0
loony=0
pinloony=100
toony=0
pintoony= 200
quater=0
pinquater=25
dimes= 0
pindimes= 10
nickel=0
pinnickel= 5


messagelist = ["Enter the the number of pennies", "Penny value should be from 0 to 1000"]

def getvalidnumber ( lowval, highval):

    global messagelist
    Innum = input (messagelist[0] ) ## messagelist[ 0, 1, 2...]
    Innum = int (Innum)
    while (Innum < lowval) or (Innum > highval): ## Same as while not
        print ( messagelist [1] )
        Innum = input (messagelist[0])
    return ( Innum )



print (getvalidnumber (0, 1000))


## Calculations

toony = penny // pintoony
premainder = penny % pintoony

loony = premainder // pinloony
premainder = premainder % pinloony  ## Run the right side then the left, "=" means the right actions apply to the left var.

quater = premainder // pinquater
premainder = premainder % pinquater

dimes = premainder // pindimes
premainder = premainder % pindimes

nickel = premainder // pinnickel
premainder = premainder % pinnickel


print ("The numbers of your toonies are ", toony)
print ("The numbers of your loonies are ", loony)
print ("The numbers of your quarters are ", quater)
print ("The numbers of your dimes are ", dimes)
print ("The numbers of your dimes are ", nickel)


