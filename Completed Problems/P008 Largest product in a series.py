#Find the greatest product of five consecutive digits in the 1000-digit number.

digit = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
#Numbers of characters in <digit>
digits = 1000
#Number of consecutive terms
consecutiveTerms = 5
#start of range
rangeMin = 0
#end of range
rangeMax = digits - consecutiveTerms
listOfTerms = []

#rangeEnd 1000 grabs <index> 999.
#   999-5 = 994 is last index.
#   994+1 = 995 = range.
#for pos in range, pos will be 0 - 995


#----INDEX----POS---VAR-CONST--i----
#   term[0] = 1st = pos0     = 0
#   term[1] = 2nd = pos0 + 1 = 1
#   term[2] = 3rd = pos0 + 2 = 2
#   term[3] = 4th = pos0 + 3 = 3
#   term[4] = 5th = pos0 + 4 = 4
#  -term[5] = 6th = pos0 + 5 = 5
#     --next value of pos--
#   term[1] = 1st = pos1     = 1
#   term[2] = 2nd = pos1 + 1 = 2
#   term[3] = 3rd = pos1 + 2 = 3
#   term[4] = 4th = pos1 + 3 = 4
#   term[5] = 5th = pos1 + 4 = 5
#  -term[6] = 6th = pos1 + 5 = 6

#           method. input (string) #string will be digit
#   FOR LOOP TO:
#       grab sting, <index> as loopvar, len = 5
#           =string[index:index+5]
#           get product of five terms and store to value, newProduct
#           if newProduct > oldProduct
#               get the five terms and store to a list           
#               5 in list. These are the 5 highest terms
#   return oldProduct as greatest product.


#--- No. ---func to grab 5 terms put into list starting from input as index [0-999]

def getGreatestProduct(digit):
    oldProduct = 0
    for index in range(rangeMin, rangeMax):
        fiveTerms = digit[index:index+5]
        newProduct = getProduct(fiveTerms)
        if determineGreater(oldProduct, newProduct, index):
            oldProduct = newProduct
    return oldProduct


gGP = getGreatestProduct

#func to determine if newProduct > oldProduct
#INPUT: oldProduct, newProduct, index
#           if it is, update list of terms
#RETURN: bool
def determineGreater(oldProduct, newProduct, index):
    if newProduct > oldProduct:
        listOfTerms = []
        listOfTerms.append(digit[index:index+5])
        return True
    return False

#func to get product of five terms,
#INPUT: string of 5 characters
#RETURN: value newProduct
def getProduct(string):
    newProduct = 1
    for si in range(0, 5):
        newProduct *= int(string[si])
    return newProduct
