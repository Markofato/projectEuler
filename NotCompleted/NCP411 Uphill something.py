#(x, y) = (2^i % n , 3^i % n)
#0 <= i <= 2n
# http://projecteuler.net/problem=411

# - Get possible coords
# - Get coords as points on graph.
# - eliminate duplicates
#from point A to B, determine derivative.
#Allow for two coordinates to be entered and return bool, T is m >= 0
#make sure AB->'(x,y) >= 0, otherwise xycoords are decreasing.
#from point 0: 0,0 ... test all points in list.
#Those that pass test, append to new list: point 1.
#from point 1: [list] run through all points that pass test,
#append to new list: point 2
#repeat until no points remaining.

#while
#   for

n = 10
i = n/2
stationCounter = 1
possibleXcoordinate = 0.0
possibleYcoordinate = 0.0
Xcoords = []
Ycoords = []
XYcoords = []
distList = []
newList = []
m = 0.0
x = 0


#input n  and return all possible x coordinates
def getXcoords(n):
    i = n/2
    for x in range(0, i+1):
        possibleXcoordinate = 2**x % n
        Xcoords.append(possibleXcoordinate)
    return Xcoords

#input n  and return all possible y coordinates
def getYcoords(n):
    i = n/2
    for x in range(0, i+1):
        possibleYcoordinate = 3**x % n
        Ycoords.append(possibleYcoordinate)
    return Ycoords
  
#takes in list and returns ln of 1st duplicate term
def whereIsDuplicateStation(coordList):
    lenOfList = len(coordList)
    for ln in range(0, lenOfList):
        if coordList[ln] in coordList[ln+1:]:
            return ln
        
#checks for 1 duplicate inside list, returns bool
def checkDuplicateStation(coordList):
    lenOfList = len(coordList)
    for ln in range(0, lenOfList):
        if coordList[ln] in coordList[ln+1:]:
            return True
    return False

#combines check, whereIs and remove to clean lists
def cleanStationList(coordList):
    while checkDuplicateStation(coordList):
        ln = whereIsDuplicateStation(coordList)
        coordList.remove(coordList[ln])
    return coordList

#takes in two points, returns gradiant
def gradiant(pointA, pointB):
    dy = pointA[0] - pointB[0]
    dx = pointA[1] - pointB[1]
    if dy == 0 or dx == 0:
        m = 0
        return m
    m = float(dy) / float(dx)
    return m

#takes in two points, returns distance between them
def getDistance(pointA, pointB):
    dy = pointA[0] - pointB[0]
    dx = pointA[1] - pointB[1]
    dSqd = dy**2 + dx**2
    distance = dSqd ** 0.5
    return distance

#takes in gradient and one set of point, prints line equation
def getLineEquation(m, pointA):
    #y = mx + b
    b = pointA[1] - m * pointA[0]
    print('y = {}x + {}'.format(m,b))

#takes in list, prints distance between [0: and all terms to :last]
def printShortestDistance(coordList):
    lenOfList = len(coordList)
    for ln in range(1, lenOfList):
        distance = getDistance(coordList[0], coordList[ln])
        print(distance, ln)
        gradList.append((distance, ln))
        
#generates new list


#takes in list assumes point [0] of list and finds first m < 0 and returns ln
def findFirstNegGrad(coordList):
    lenOfList = len(coordList)
    for ln in range(1, lenOfList):
        m = gradiant(coordList[0],coordList[ln])
        if m < 0:
            return ln

#checks for negative gradiants returns list [1:]
def checkNegGradiant(coordList):
    lenOfList = len(coordList)
    for ln in range(1, lenOfList):
        m = gradiant(coordList[0],coordList[ln])
        if m < 0:
            return True
    return False

#combines check, ln and remove to remove neg grads
def trimNegGradiant(coordList):
    while checkNegGradiant(coordList):
        ln = findFirstNegGrad(coordList)
        coordList.remove(coordList[ln])

#appends lists
def genShortestDistanceList(coordList):
    lenOfList = len(coordList)
    for ln in range(1, lenOfList):
        distance = getDistance(coordList[0], coordList[ln])
        distList.append((distance, ln))
    coordList = zip(coordList[1:], distList)
    return coordList

g = genShortestDistanceList #short hand.
        
#Proceed to next Station; takes list [0:] makes new list
def nextStation(coordList):
    x = 1 #at pos [0]
    while len(coordList) > 0:
        printShortestDistance(coordList)
        trimNegGradiant(coordList)
        coordList.remove(coordList[0])
        x += 1
    return x
    
#creates XYcoords
def S(n):
    getXcoords(n)
    getYcoords(n)
    XYcoords = zip(Xcoords, Ycoords)
    cleanStationList(XYcoords)
    return XYcoords

XYcoords = S(n)
distList = g(XYcoords)

#sorts by distance
sorted(distList, key=lambda distList:distList[1][0])

