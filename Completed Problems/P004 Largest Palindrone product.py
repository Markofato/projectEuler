#A palindromic number reads the same both ways.
#The largest palindrome made from the product of
#two 2-digit numbers is 9009 = 91 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
import cProfile

#numOfDigits = 2 | a,b = 99, 91 | p = 9009
#Was using highest x value:
#numOfDigits = 3 | a,b = 995, 583 | p = 580085 (seems too low.)
#numOfDigits = 3 | a,b = 913, 993 | p = 906609  <--
#numOfDigits = 4 | a,b = 9999, 9901 | p = 99000099

#numOfDigits = 3, expecting a,b = 9xx, 9xx. b = 5xx..
#suspect palinTester(x, y) is giving a false False
#palinTester worked fine, replaced with single line.
#Problem was palinGenerator, returned last palin generated.
#presumed last generated would be the greatest value.

#wrong because  x = [0], y = [0 -> end]
#               x = [1], y = [0 -> end]
#if greatest term was   x[0]*y[9] = 202
#if last term given is  x[1]*y[5] = 101
#is returning last palin with highest x value.
# [corrected]

#inputs as 10 ** numOfDigits

#checks for palendromic properties regarding 1 term only
#( palinToTest[lhs] == palinToTest[rhs] )returns T or F.
def termsPalindromic(palinToTest, lhs, rhs): #made redundant..
    #print(palinToTest[lhs], palinToTest[rhs])
    if palinToTest[lhs] == palinToTest[rhs]:
        return True
    else:
        return False

    
#tests if palindrone for input as x*y
#with p as str: ( p == p[::-1]: )returns T or F
def palinTester(x, y): #made redundant..
    palinToTest = x*y
    p = str(palinToTest)
    #print(p)
    lp = len(p)
    for lhs in range(0, lp/2):
        rhs = -(lhs + 1)
        if p[lhs] == p[rhs]:
            pass
        else:
            return False
    return True

#tests if palindrone for input as z
def miniPalinTester(z):
    palinToTest = z
    p = str(palinToTest)
    print(p)
    lp = len(p)
    for lhs in range(0, lp/2):
        rhs = -(lhs + 1)
        print(lhs, rhs)
        if p[lhs] == p[rhs]:
            pass
        else:
            return False
    return True

#>>> miniPalinTester(99000099) while printing(lhs, rhs)
#99000099,(0, -1),(1, -2),(2, -3),(3, -4)
#True

#>>> miniPalinTester(9901099) while printing(lhs, rhs)
#9901099,(0, -1),(1, -2),(2, -3)
#True

#>>> miniPalinTester(990221099) while printing(lhs, rhs)
#990221099,(0, -1),(1, -2),(2, -3),(3, -4)
#False

def palinGenerator(numOfDigits): #as in, 2 digit eg 91x99 = 9009
    pTop = 0
    for x in range(10**(numOfDigits-1), 10**(numOfDigits)):
        for y in range(10**(numOfDigits-1), 10**(numOfDigits)):
            p = x*y
            if pTop < p:
                if str(p) == str(p)[::-1]:
                    a, b = x, y
                    pTop = p
    return a, b, a*b
