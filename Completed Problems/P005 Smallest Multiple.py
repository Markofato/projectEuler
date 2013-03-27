#What is the smallest positive number that is evenly divisible
#by all of the numbers from 1 to 20?


rangeMax = 20
rangeMin = 1
stopLoop = False
if rangeMax < 10:
    step = 2
    x = 2
else:
    step = 10
    x = 10
    
#nums 1 - 10 should return 2520.
#nums 1 - 11 returned 27720
#nums 1 - 12 returned 27720
#nums 1 - 13 returned 360360
#nums 1 - 14 returned 360360
#nums 1 - 15 returned 360360
#nums 1 - 16 returned 720720
#nums 1 - 17 returned 12252240
#nums 1 - 18 returned 12252240
#nums 1 - 19 returned 232792560
#nums 1 - 20 returned 232792560 is correct!

def isEvenlyDivisble(x):
    return x % divisor == 0

while stopLoop == False:
    for divisor in range(rangeMax, rangeMin-1, -1):
        if isEvenlyDivisble(x):
            stopLoop = divisor == rangeMin
        else:
            x += step
            break
print("x = {0}".format(x))
