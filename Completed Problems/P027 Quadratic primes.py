#[1011, (-999, 61)] as first result.

#checks if prime
def primeChecker(numberToCheck):
    for div in range(2, numberToCheck):
        if numberToCheck % div == 0: return False
    return True

#generates num to check if prime
def quad(a, b, n):
    num = abs(n*n + a*n + b)
    return num

#counts n, number of consecutive primes
def consecutivePrimes(a, b):
    n = 0
    while n != -1:
        num = quad(a, b, n)
        if primeChecker(num):
            n+=1
        else:
            return n
        
def find_ab():
    nab = [0, 0]
    for a in range(1000,-1000, -1):
        for b in range(-1000, 1000):
            n = consecutivePrimes(a, b)
            if n > nab[0]:
                nab = [n, (a, b)]
                print(nab)
    return nab
