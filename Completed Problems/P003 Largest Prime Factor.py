__author__ = 'God'
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#prime number that evenly divide a number



import time

import itertools
range = lambda stop: iter(itertools.count().next, stop)

x = 600851475143
#6857!
y = 13195

#Code is very slow. testing computation speed
start_time = time.time()

def primeChecker(numberToCheck):
    for div in range(numberToCheck):
        if div == 0 or div == 1:continue
        if numberToCheck % div == 0: return False
    return True

def highestEvenlyDivisbleNumber(numberToDivide):
    x = 0
    for divisor in range(numberToDivide/2): #300425737571L
        #range = lambda doesn't allow for 2 parameters and 0 gives error
        if divisor == 0:continue 
        ###
        #test if with %==0 and primeChecker | time: ~4.45 per 10^7
        if numberToDivide % divisor == 0 and primeChecker(divisor):
            x = divisor
        ###
        #testing nested if primeChecker: %==0 | 'x = 10^3' time = ~3x^2
        #if primeChecker(divisor):
        #    if numberToDivide % divisor == 0:
        #        x = divisor
        #    else:
        #        continue
            
        ####
        #testing nested if %==0: primeChecker | time: ~4.632 per 10^7
        #if numberToDivide % divisor == 0:
        #    if primeChecker(divisor):
        #        x = divisor

        #every 100,000,000 numbers tested, returns divisor and current x
        if divisor % 100000000 == 0:
            elapsed_time = time.time() - start_time
            print(divisor, x, elapsed_time)
    return x

num = highestEvenlyDivisbleNumber(x)
print(num)


def highestEvenlyDivisbleNumber(numberToDivide):
    x = 0
    for divisor in range(numberToDivide/2): #300425737571L
        #range = lambda doesn't allow for 2 parameters and 0 gives error
        if divisor == 0:continue 
        ###
        #test if with %==0 and primeChecker | time: ~4.45 per 10^7
        if numberToDivide % divisor == 0 and primeChecker(divisor):
            x = divisor
        ###
        #testing nested if primeChecker: %==0 | 'x = 10^3' time = ~3x^2
        #if primeChecker(divisor):
        #    if numberToDivide % divisor == 0:
        #        x = divisor
        #    else:
        #        continue
            
        ####
        #testing nested if %==0: primeChecker | time: ~4.632 per 10^7
        #if numberToDivide % divisor == 0:
        #    if primeChecker(divisor):
        #        x = divisor

        #every 100,000,000 numbers tested, returns divisor and current x
        if divisor % 100000000 == 0:
            elapsed_time = time.time() - start_time
            print(divisor, x, elapsed_time)
    return x

#2012 attempt..#
#######################
#######ATTEMPT 1#######

#cap=13195
#def testPrime(num):
#    if cap % num == 0:
#        return True
#    return False

#def numbers(cap):
#    currentNumber = 1
#    while currentNumber <= cap:
#        if testPrime(currentNumber):
#            largestPrime = currentNumber
#        currentNumber += 1
#        print (largestPrime)
#    return largestPrime


#print (numbers(13195))

#######################

#def largestPrimeNumber(number):
#    start = 1
#    while start <= number:
#        if testPrimeNumber(start):
#            start += 1
#        break
#    return

#def testPrimeNumber(num):
#    if (num)==1:
#        return True
#    n=1
#    primeTesterValue = 0
#    while n <= num:
#        if num % n == 0:
#            primeTesterValue += 1
#            n += 1
#        else:
#            n += 1
#    if primeTesterValue == 2:
#        return True
#    else:
#        return False


#print (testPrimeNumber(5))
#def largestPrimeFactor(number):

