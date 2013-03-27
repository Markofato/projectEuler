#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import itertools
import listPrimes
import time
import tester
"""

142913828922
142913828922L


"""


#Possible slowest func.
def primeChecker(numberToCheck):
    for div in range(2, numberToCheck):
        if numberToCheck % div == 0: return False
    return True

#SLOW. input max range, returns sumation of primes under range
def getAllPrimes(Maximum):
    total = 2
    for num in range(3, Maximum+1, 2):
        if primeChecker(num):
            total += num            
    return total

#alt method via checking with list - doesn't count 2
def sumationPrimesIndexCut(Maximum):
   primeList = listPrimes.returnList()
   total = 2
   for num in range(1, Maximum+1, 2):
       if str(num) in primeList:
           total += num
           index = primeList.index(str(num))
           primeList = primeList[index:]
   return total


"""
def sumationPrimes(Maximum):
   primeList = listPrimes.returnList()
   total = 2
   start_time = time.time()
   for num in range(1, Maximum+1, 2):
       if str(num) in primeList: #make this a func to return index if true
           total += num
   return total, (time.time()-start_time)
"""

#input list of primes, return sum of first to end of list
def sumOfList(inputList):
    sumOf = 0
    for ix in range(0, len(inputList)):
        sumOf += inputList[ix]
    return sumOf

#input list of primes, return sum of all under X
def sumUnderX(num):
    inputList = listPrimes.returnList()
    sumOf = 0
    for ix in range(len(inputList)):
        if int(inputList[ix]) <= num:
            sumOf += int(inputList[ix])
        else:
            break
    return sumOf
'''
#func for printing strings
def results(func, test):
    print('testing {}:'.format(func.func_name))
    #for t in test:  uncomment when text() has more then 1 input
    start_time = time.time()
    print("{} gave {} in {}".format(test,func(test),str(round(time.time()-start_time,3)) + ' seconds'))
 
#func for testing computation times
def test(x):# ,y,z):
    results(sumUnderX, x)#x, y, z])
    #results(getAllPrimes, x)#[x, y, z])
    #results(sumationPrimesIndexCut, x)#[x, y, z])
    return 'Finished testing.'




#func for printing strings
def results((a,b,c),(d,e,f),(h,i,j),(k,l,m), x,y,z):
    print('testing getAllPrimes:{0}\
{1} at {4}{0}\
{2} at {5}{0}\
{3} at {6}{0}'.format('\n', a[1], b[1], c[1], x,y,z))
    print('testing sumationPrimes:{0}\
{1} at {4}{0}\
{2} at {5}{0}\
{3} at {6}{0}'.format('\n', d[1], e[1], f[1], x,y,z))
    print('testing sumationPrimesIndexCut:{0}\
{1} at {4}{0}\
{2} at {5}{0}\
{3} at {6}{0}'.format('\n', h[1], i[1], j[1], x,y,z))
    print('testing sumUnderX:{0}\
{1} at {4}{0}\
{2} at {5}{0}\
{3} at {6}{0}'.format('\n', k[1], l[1], m[1], x,y,z))
    return

#func for testing computation times
def test(x,y,z):
    g = getAllPrimes
    s = sumationPrimes
    i = sumationPrimesIndexCut
    u = sumUnderX
    a = (g(x), g(y), g(z))
    b = (s(x), s(y), s(z))
    c = (i(x), i(y), i(z))
    d = (u(x), u(y), u(z))
    return results(a,b,c,d, x,y,z)
          
'''
