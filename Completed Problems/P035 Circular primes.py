import listPrimes
import tester

primeList = listPrimes.returnList()

#input prime and shift
def buildCoder(number, shift):
    #numphabet = ('1234567890')
    numphabet = str(number)
    cipher = {}

    for n in range(len(numphabet)):
        plainNumber = numphabet[n]
        x = shift+n-len(numphabet)
        if n+shift < len(numphabet): x = shift+n
        cipherNumber = numphabet[x]
        cipher[plainNumber] = cipherNumber
    return cipher

#input STRING and cipher, return prime with shift
def applyCoder(text, coder):    
    cipherText = list(text)
    for index in range(len(text)):
        if text[index] in coder.keys():
            cipherLetter = coder[text[index]]
        else:
            cipherLetter = text[index]
        cipherText[index] = cipherLetter
    cipherText = ''.join(cipherText)
    return cipherText

def applyShift(prime, shift):
    prime = list(prime)
    prime.append(prime[0])
    rotation = ''.join(prime[1:])
    return rotation

#checks if circular, input prime as string and primelist, return bool
def isCircular(prime, primeList):
    for shift in range(0,len(prime)+1):
        #cipher = buildCoder(prime, shift)
        #rotation = applyCoder(prime, cipher)
        prime = applyShift(prime, shift)
        #print(rotation)
        if len(str(int(prime))) != len(prime): return False
        if str(int(prime)) not in primeList:
            return False
    return True

#input x index starting at 0, length of prime and primeList,
#   returns first and last index
#returns all prime numbers of that length
def getIndexs(x, pLength, primeList):
    while len(primeList[x]) < pLength:
        x+=1
    y = x
    while len(primeList[y]) < pLength+1:
        y+=1
    return [x,y]

def sList(x, y, primeList):
    shortList = primeList[x:y]
    return shortList

#progressive, returns index[1] and plen aswell as list.
def shortList(lengthOfPrimes, indeX, primeList):
    plen = lengthOfPrimes
    index = getIndexs(indeX, plen, primeList)
    shortList = sList(index[0], index[1], primeList)
    print(plen, index[0], index[1], primeList[index[0]], primeList[index[1]], len(shortList))
    indeX = index[1]
    return plen, shortList, indeX

'''
def slWrap(pLen, prime):
    if plen != len(prime):
        plen = len(prime)
        index = getIndexs(x, plen, primeList)
        shortList = sList(index[0], index[1], primeList)
        x = index[1]
'''
    
#grabs prime
def primesUnderX(num):
    n,plen,indeX=0,0,0
    primeList = listPrimes.returnList()
    for ix in range(len(primeList)):
        prime = primeList[ix]
        if int(prime) <= num:
            if plen != len(prime):
                print(n)
                shortenedList = shortList(len(prime),indeX,primeList)
                plen, indeX = shortenedList[0], shortenedList[2]
            if isCircular(prime, shortenedList[1]):
                print(prime)
                n+=1
        else:
            return n
    return 




p = primesUnderX


