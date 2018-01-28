# User enter a num
# Find all the factors, into a list
# Count factors
# Decide prime or composite
# Print innum, factors

def getFactors ():
    numfactor = 0
    factor = []
    innum = int(input("Enter a number:"))
    for i in range (1, innum+1):
        if innum % i == 0:
            factor.append(i)
            numfactor = numfactor + 1

    if numfactor == 2:
        print (innum, "is a prime number")
    elif numfactor == 1:
        print (innum, "is neither a prime nor composite number")
    else:
        print (innum, "is a composite number")

    print ("Its factors are", factor)

    return (innum, factor)


(num, list1) = getFactors()



