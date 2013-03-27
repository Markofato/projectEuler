import listPrimes

#(997651, 543)

primeList = listPrimes.returnList()
underList = listPrimes.underList
iP = listPrimes.isPrime
#get all primes under n digits
def getHighestPrime(n):
    shortList = underList(n)
    hPrime = [0,0]
    for prime in shortList[::-1]:
        nPrime = consecutiveUnder(int(prime),shortList)
        #print nPrime
        if nPrime[1] > hPrime[1]:
            hPrime = nPrime
            print(hPrime)
    return hPrime

#adds up primes from [0]->[index] until  each > or == prime
def consecutiveUnder(prime, primeList):
    #prime = primeList[index]
    index = primeList.index(str(prime))
    for i in range(index+1):
        sumOf = 0
        numConsec = 0
        for p in primeList[i:]:
            sumOf+=int(p)
            numConsec+=1
            if sumOf == prime: return prime, numConsec
            if sumOf > prime: break


