import listPrimes
import tester
import time

primeList = listPrimes.returnList()


#input prime as string, removes LEFT to RIGHT [1:]
def truncateLTR(prime, primeList):
    #print(prime)
    if len(prime) == 1: return True
    if prime[1:] in primeList: return truncateLTR(prime[1:], primeList)
    return False

#input prime as string, removes LEFT to RIGHT [1:]
def truncateRTL(prime, primeList):
    #print(prime)
    if len(prime) == 1: return True
    if prime[:-1] in primeList: return truncateRTL(prime[:-1], primeList)
    return False


def truncate(prime, primeList):
    if truncateLTR(prime, primeList) == False: return False
    if truncateRTL(prime, primeList) == False: return False
    return True

#input prime as string, removes LEFT to RIGHT [1:]
def parallelTruncate(primeL, primeR, primeList):
    if len(primeL) == 1: return True
    if primeL[1:] in primeList:
        if primeR[:-1] in primeList:#\
       #and primeL[:-1] in primeList and primeR[1:] in primeList:
            return parallelTruncate(primeL[1:], primeR[:-1], primeList)
        return False
    return False
        
        
def truncateLTR(prime, primeList):
    #print(prime)
    if len(prime) == 1: return True
    if prime[1:] in primeList: return truncateLTR(prime[1:], primeList)
    return False

#input prime as string, removes LEFT to RIGHT [1:]
def truncateRTL(prime, primeList):
    #print(prime)
    if len(prime) == 1: return True
    if prime[:-1] in primeList: return truncateRTL(prime[:-1], primeList)
    return False


ltr = truncateLTR
rtl = truncateRTL

def getIndexs(x, pLength, primeList):
    while len(primeList[x]) < pLength:
        x+=1
    y = x
    while len(primeList[y]) < pLength+1:
        y+=1
    return [x,y]

def sList(x, y, primeList):
    shortList = primeList[:y]
    return shortList

#checks if truncatable, input prime as string and primelist, return bool
def isTruncatable(prime, primeList):
    notTruncatable = ['2','3','5','7']
    if prime in notTruncatable: return False
    if parallelTruncate(prime, prime, primeList): return True
    #if truncate(prime, primeList): return True
    #if ltr(prime, primeList) and\
    #           rtl(prime, primeList):
    #        return True
    
    return False

#grabs prime
def truncatablePrimes():
    start_time = time.time()
    n,x,plen=0,0,0
    sumOftruncatablePrimes = 0
    primeList = listPrimes.returnList()
    for ix in range(len(primeList)):
        if n < 11:
            prime = primeList[ix]
            if plen != len(prime):
                plen = len(prime)
                index = getIndexs(x, plen, primeList)
                shortList = sList(index[0], index[1], primeList)
                #print(plen, index[0], index[1], primeList[index[0]], primeList[index[1]], len(shortList))
                x = index[1]
            if isTruncatable(prime, shortList):
                n+=1
                print(n, prime)
                sumOftruncatablePrimes+=int(prime)
        else:
            return sumOftruncatablePrimes, n, round(time.time() - start_time,1)
    return 

tp = truncatablePrimes

