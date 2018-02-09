##Evelyn Li
##April 26, 2017

# Enter the names of the student and marks
# Find the class average and highest and lowest marks
# Generate a sorted mark list (choose to sort by name or mark)

##Variable map
##NAME                       PURPOSE                            TYPE                               RAMGE
##studentname            Ask for stud name                     string                              none
##highmark               Highest mark valid to enter            int                                100
##lowmark                Lowest mark valid to enter             int                                 0
##classavg               Average of the class                   int                             100 to 0
##numstud                Number of students                     int                              32 to 0
##stumark                Ask for student mark                   int                             100 to 0
##totalmarkall           Total mark in class                    int                                none
##lowest                Lowest mark in class                    int                                100
##highest               Highest mark in class                   int                                 0

#Declear variables
studname        = ""
highmark        = 100
lowmark         = 0
classavg        = 0
numstud         = 0
stumark         = 0
totalmarkall    = 0
lowest          = 100
highest         = 0
newlist         = [0, 0]
finallist       = [0, 0]


#Declare functions
def validData(low, high, message):
    value = int(input(message))
    valid = (value >= low) and (value <= high)
    while not valid:
        print ("Error, incorrect value entered, Try again")
        value = int(input("Please enter again:" ))
        valid = (value >= low) and (value <= high)
    return(value)


#Function for sorting in descending order
def bubbleSort (list, limit, message1):
    which= input (message1)
    which= int (which)
    for i in range (1, limit):
        for j in range (0, limit-i):
            if list [j][which]< list [j+1][which]:
                list[j], list [j+1]= list [j+1], list[j]
            if  list [j][which]> list [j+1][which]:
                break
    return list



#Enter number of students
numstud = validData(0, 32, "PLease enter the number of students")


#Enter student mark
newlist = [[0]*2 for i in range (numstud)]
for i in range (numstud):                              #input section
    studname  = input("Enter the student's name:")
    newlist [i][0]= studname


    stumark  = validData(lowmark,highmark,"Enter the mark of the student (between 1 and 100)")
    newlist [i][1]= stumark

                                                      #output section
    print (studname, "'s mark is ",stumark)

    if stumark < lowest:                              #calculation section
        lowest = stumark
    if stumark > highest:
        highest = stumark

    totalmarkall = totalmarkall + stumark


# Class avg
classavg = totalmarkall / numstud
print (classavg," is the average of the class")

# Highest lowest
print (highest," is the highest mark in the class")
print (lowest," is the lowest mark in the class")

# Name List
finallist = (bubbleSort(newlist, numstud, "What do you want to sort with? Enter 0 for name and 1 for marks."))
print ('\n'.join(map(str, finallist)))




