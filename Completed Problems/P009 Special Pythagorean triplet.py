#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

#a^2 + b^2 = c^2
#For example,   3^2 + 4^2 = 5^2.
#                9  + 16  = 25  

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#for a  :
#   for b   :
#       for c   :
#           if a+b+c = 1000 and a^2 + b^2 = c^2
#               return a, b, c      - Only one combination exists.

#ans = a*b*c

posSums = []
SqsFromPosSums = []
posSqs = []
SumsFromPosSqs = []

#all possible a^2 + b^2 == c^2
def allPosSqs(rangeMin, rangeMax):
    for a in range(rangeMin, rangeMax):
        for b in range(a, rangeMax):
            for c in range(b, rangeMax):
                if a**2 + b**2 == c**2:
                    posSqs.append((a,b,c))
                    #print(a,b,c)
    return posSqs

aps = allPosSqs

#all possible a+b+c == sumOf into list
def allPosSums(sumOf):
    for a in range(1, sumOf+1):
        for b in range(a+1, sumOf+1):
            for c in range(b+1, sumOf+1):
                if a+b+c == sumOf:
                    posSums.append((a, b, c))
                    #print(pos1)
    return posSums

#checks list for a^2 + b^2 == c^2
def checkForSqs(inputList):
    il = inputList
    for ix in range(0, len(il)):
        if il[ix][0]**2 + il[ix][1]**2 == il[ix][2]**2:
            SqsFromPosSums.append((il[ix][0], il[ix][1], il[ix][2]))
            print((il[ix][0], il[ix][1], il[ix][2]))
    

#checks list for a+b+c == sumOf
def checkForSums(inputList, sumOf):
    il = inputList
    for ix in range(0, len(il)):
        if il[ix][0] + il[ix][1] + il[ix][2] == sumOf:
            SumsFromPosSqs.append((il[ix][0], il[ix][1], il[ix][2]))
            ans = (il[ix][0] * il[ix][1] * il[ix][2])
            return ans
    
