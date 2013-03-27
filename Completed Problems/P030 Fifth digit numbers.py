"""
Surprisingly there are only three numbers that can be
written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as
the sum of fifth powers of their digits.
"""
# rangeMax as 10,000 = [4150, 4151]
# rangeMax as 100,000 = [4150, 4151, 54748, 92727, 93084]
# rangeMax as 100,000,000 = [4150, 4151, 54748, 92727, 93084, 194979]
#       443839
#range: all nums excluding 1

numsWithEqValue = []

#constructs a dictionary of numbers 0 to 9 to the power of nth
def constructDict(nth):
    nums = [str(x) for x in range(0,10)]
    powers = [x**nth for x in range(0,10)]
    ntoNth = dict(zip(nums,powers))
    return ntoNth

#takes in num and returns value of numbers to the fifth
#   num can be int or string
def getValue(num, ntoNth):
    strNum = str(num)
    total = 0
    for n in strNum:
        total += ntoNth[n]
    return total

#takes in num as int or string, returns bool if it can be written as
#   the sum of it's digits to the fifth
def checkValue(num, ntoNth):
    if num == getValue(num, ntoNth):
        return True
    else:
        return False

#excludes num 1 since 1=1**x
def checkNumsUpTo(rangeMin, rangeMax, nth):
    ntoNth = constructDict(nth)
    for num in range(rangeMin, rangeMax):
        if checkValue(num, ntoNth):
            numsWithEqValue.append(num)
    return numsWithEqValue

    
