#What is the 10 001st prime number?
import xth

#10001st prime is 104743.

def main(endPrimeNumber):
    
    num = findPrimeNumber(endPrimeNumber)

    


def primeChecker(numberToCheck):
    for div in range(2, numberToCheck):
        if numberToCheck % div == 0: return False
    return True

def findPrimeNumber(endPrimeNumber):
    num = 1
    primeNumbersCounted = 0
    while primeNumbersCounted != endPrimeNumber:
        num += 1
        if primeChecker(num): primeNumbersCounted += 1
    print("The {} prime number is: {}".format(xth.xth(primeNumbersCounted), num))
    return


