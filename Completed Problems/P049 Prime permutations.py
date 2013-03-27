'''The arithmetic sequence, 1487, 4817, 8147, in which each of
the terms increases by 3330, is unusual in two ways: (i) each of
the three terms are prime, and, (ii) each of the 4-digit numbers
are permutations of one another.

There are no arithmetic sequences made up of three
1-, 2-, or 3-digit primes, exhibiting this property, but there is
one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms
in this sequence?


A   <    B   <    C
A + n == B
         B + n == C

A, B, C are all prime

A, B, C = {x,y,z,u}

'''
import listPrimes
primeList = listPrimes.returnList()




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

#checks if C and A contain the same numbers
def checkXinY(numC, numA):
    C = sorted(list(str(numC)))
    A = sorted(list(str(numA)))
    if [a for a in A] == [c for c in C]:
        return True
    return False

#returns
def findB():
    sList = shortList(4)
    #gets C from primeList 9999->1000
    for C in sList[::-1]:

        #gets A from primeList 1000->9999
        for A in sList:

            #sorts C&A. checks c in C == a in A
            if checkXinY(C, A):
                for n in range(1,4500):
                    C, A = int(C), int(A)

                    #gets B by finding where A+n == C-n
                    if 2*n == C - A:
                        B = A + n
                        
                        #sorts a in A == b in B and B is prime
                        if checkXinY(A,B) and str(B) in sList:
                            if B != 4817: return ("A = {1}.\nB\
= {2} = A + n = C - n.\nC = {3}\n{0} = n".format(n,A,B,C))
    return 'Done.'
