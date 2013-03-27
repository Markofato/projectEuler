#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025

#Hence the difference between the
#sum of the squares of the first ten natural numbers and the
#square of the sum is 3025 - 385 = 2640.

#Find the difference between the
#sum of the squares of the first one hundred natural numbers and the
#square of the sum.

#25164150

#finds the sum of the squares with input as the range, from 1 to input inclusive
def sigmaOfSquares(firstXnaturalNumbers):
    sumOf = 0
    for n in range(1, firstXnaturalNumbers+1):
        sumOf += n**2
    return sumOf

def squareOfSigma(firstXnaturalNumbers):
    sumOf = 0
    for n in range(1, firstXnaturalNumbers+1):
        sumOf += n
        squared = sumOf**2
    return squared

#finds the difference with input as the range, from 1 to input inclusive
def difference(firstXnaturalNumbers):
    sumOftheSquares = sigmaOfSquares(firstXnaturalNumbers)
    squareOftheSum = squareOfSigma(firstXnaturalNumbers)
    difference = squareOftheSum - sumOftheSquares
    return difference
