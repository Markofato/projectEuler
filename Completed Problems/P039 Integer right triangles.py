

def rightAngleChecker(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


def numCombGenerator(n):
    for a in range(1, n/2):
        for b in range(a, n/2):
            c = n - b - a
            yield a, b, c


def run(pMax):
    termData = ['p', 0, 0]
    for p in range(1, pMax + 1):
        termData[2] = 0
        for a, b, c in numCombGenerator(p):
            if rightAngleChecker(a, b, c):
                termData[2] += 1
        if termData[1] < termData[2]:
            termData[:2] = [p, termData[2]]
    return termData



print run(1000)


#840 with 8 combinations


import time

def rightAngleChecker(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


def numCombGenerator(n):
    for a in range(1, n/2):
        for b in range(a, n/2):
            c = n - b - a
            yield a, b, c


def run(pMax):
    startTime = time.time()
    termData = ['p', 0, 0]
    for p in range(1, pMax + 1):
        termData[2] = 0
        for a, b, c in numCombGenerator(p):
            if rightAngleChecker(a, b, c):
                termData[2] += 1
                print(p, a, b, c)
        if termData[1] < termData[2]:
            termData[:2] = [p, termData[2]]
    return termData, time.time() - startTime



print run(1000)


