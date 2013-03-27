#digit = str(2**1000)
import math

digit = str(math.factorial(100))
total= 0


for i in range(0, len(digit)):
    total += int(digit[i])
print(total)
