'''Define Co(n) to be the maximal possible sum of a set of
mutually co-prime elements from {1, 2, ..., n}.
For example Co(10) is 30 and hits that maximum on the
subset {1, 5, 7, 8, 9}.

You are given that Co(30) = 193 and Co(100) = 1356.

Find Co(200000).'''

#Number of terms seems to be n/2 +1...
#n = 10      gives       6  terms
#n = 30      gives      16  terms
#n = 100     gives      51  terms
#n = 1000    gives     501  terms
#n = 200,000 gives 100,001  terms?

#n number of terms. divide by 2, + n[-2] (largest even term.)
import tester
#Co(10)  = 30       <3

#Co(30)  = 193      <3


#REMOVE ALL EVEN TERMS EXCEPT FOR THE LAST FOUND ONE
#   Then apply trim.

#Co(100) = 1025.    difference of 331

#Co(100) = 1222.    difference of 134
'''
[1, 29, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
85, 89, 91, 95, 97, 98, 99]
1398
[1, 29, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
XX, 89, XX, 95, 97, 98, 99]
1222

[1, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 95, 97, 98, 99]
'''
#Co(100) = 1193.    difference of 163
n = 10
gcdList = [1]
testList = []

#input number and tests against gcdList if gcd == 1
def gcdwList(number):
    for n in gcdList:
        if n % number == 0: return False
    return True


#when gcd(a,b) = 1, add highest to gcdList if unique
def gcdMethOne(A,B):
    #when A == B, gcd is not 1
    if A == B: return 
    #gets the higher of the terms
    H, L = A, B
    if A < B: H, L = B, A
    #runs range, 2 to H inclusive.
    #       (A,B)=(2,5) | r= 2,3,4,5
    #       (A,B)=(4,9) | r= 2,3,4,5,6,7,8,9
    #           index[0] is always 1
    for n in range(2, H):
        divA = A % n
        divB = B % n
        #if A%n == B%n == 0, gcd is n
        if divA + divB == 0:
            #print('fail')
            #if gcd = 1, add A and B to testList if unique.
            if A not in testList and A % 2 != 0: testList.append(A)
            if B not in testList and B % 2 != 0: testList.append(B)
            return
        
    #if gcd(A or B, for n in gcdList) == 1, add to list.
        #Does NOT add even terms to gcdList
    #print(A,B, gcdList)
    if gcdwList(A) and A % 2 != 0: gcdList.append(A)
    if gcdwList(B) and B % 2 != 0: gcdList.append(B)

#input A,B   if gcd != 1,   discard L
#       Does not maximise sum. 
def trim(A, B):
    #gets the higher of the terms
    H, L = A, B
    if A < B: H, L = B, A
    for n in range(2, H+1):
        divA = A % n
        divB = B % n
    #print(H, L, divH, divL)
        if divA + divB == 0:
            if L in gcdList: gcdList.remove(L)
            if L not in testList: testList.append(L)
    return

def applyTrim(sgcdList):
    for indexX in range(len(sgcdList)-1,0, -1):
        for indexY in range(1,indexX):
            trim(sgcdList[indexX],sgcdList[indexY])
    sgcdList = sorted(gcdList)
    #print(sgcdList)
    return sgcdList[:]

#cleans the testList
def cleanTL(testList, gcdList):
    testList.sort()
    gcdList.sort()
    for t in gcdList:
        if t in testList: testList.remove(t)
    return testList

def Co(n):
    #for {1,2,3,...,n}
    #   x value as n-1 -> 3
    for x in range(n-1,3,-1):
        #   y value is      2+1, 3+1, 4+1, ... ,n
        for y in range(x-1, 2, -1):
            #from x as 2, y goes n-2 to 2, then x steps.
            gcdMethOne(x,y)

    gcdList.append(n-2)
    sgcdList = sorted(gcdList)
    gcdList.sort()
    sgcdList = applyTrim(sgcdList)

    #print(sgcdList)

    MaxSum = 0
    for t in gcdList:
        MaxSum+=t
    print(MaxSum)

    cleanTL(testList, gcdList)
    print(gcdList)
    print(len(gcdList))
    print(testList)
    print(len(testList))
    return
'''
    for indexX in range(len(sgcdList)-1,0, -1):
        for indexY in range(1,indexX):
            trim(sgcdList[indexX],sgcdList[indexY])
    sgcdList = sorted(gcdList)
    print(sgcdList)
    MaxSum = 0
    for t in sgcdList:
        MaxSum+=t
    print(MaxSum)
    return MaxSum
'''
Co(10)