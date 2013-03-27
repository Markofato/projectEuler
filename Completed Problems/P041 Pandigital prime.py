import itertools
import listPrimes
import tester
cond = ['1','2','3','4','5','6','7','8','9']

t = tester.t

#7652413

num = sorted('743621')
def checkPandigital(num):
    cond = ['1','2','3','4','5','6','7','8','9']
    num = sorted(list(str(num)))
    i = len(num)
    if [n for n in num]==[c for c in cond[:i]]: return True
    return False

#checks if it is prime
def isPrime(number):
    if number % 2 == 0:
        return False
    else:
        for div in range(2, int(number**0.5)+1):
            if number % div == 0:
                return False
    return True

def getIndexs(x, pLength, primeList):
    while len(primeList[x]) < pLength:
        x+=1
    y = x
    while len(primeList[y]) < pLength+1:
        y+=1
    return [x,y]

def trimList(x, y, primeList):
    shortList = primeList[x:y]
    return shortList

def shortList(lengthOfPrimes):
    primeList = listPrimes.returnList()
    x = 0
    plen = lengthOfPrimes
    index = getIndexs(x, plen, primeList)
    sList = trimList(index[0], index[1], primeList)
    return sList
           
c = checkPandigital

#range should be 987,654,321 -> downwards with step 2
#memory demand too high.
def start():
    

    for p in xrange(987654323,740740700,-2):
        if checkPandigital(p):
            if isPrime(p):
                return p
    print("Not in first increment.")
    for p in xrange(740740741,493827160,-2):
        if checkPandigital(p):
            if isPrime(p):
                return p
    print("Not in second increment.")
    for p in xrange(493827161,246913580,-2):
        if checkPandigital(p):
            if isPrime(p):
                return p
    print("Not in third increment.")
    for p in xrange(246913581,100000000,-2):
        if checkPandigital(p):
            if isPrime(p):
                return p
    print("Not in fourth increment.")
    print("Stopped testing 9 digits.")
    sList = shortList(8)
    for p in sList[::-1]:
        if checkPandigital(p):
            return p
    print("Not in 8 digits.")
    print("Testing 7 digits")
    sList = shortList(7)
    for p in sList[::-1]:
        if checkPandigital(p):
            return p
    print("Testing 6 digits")
    sList = shortList(6)
    for p in sList[::-1]:
        if checkPandigital(p):
            return p
    return "No pandigital prime found"
