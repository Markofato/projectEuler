
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] <- complete range
#[1, 2, 3, 4, 5, 6, 7] <- range for gLterms
#{1: 1, 2: 1024, 3: 59049, 4: 1048576, 5: 9765625, 6: 60466176, 7: 282475249} <- dict
#3,833,759,992,447,475,122,176L <- total number of pos
#3.834 * (10 ** 21)
# find where top 10 == 70. return gLterm if gLterm != 1;
#                gLterm is key for it's multiplier of outcomes.

'''
def start():
    num = 0
    for a in res:
        for b in res:
            for c in res:
                for d in res:
                    for e in res:
                        for f in res:
                            for g in res:
                                for h in res:
                                    for i in res:
                                        for j in res:
                                            for k in res:
                                                for l in res:
                                                    for m in res:
                                                        for n in res:
                                                            for o in res:
                                                                for p in res:
                                                                    for q in res:
                                                                        for r in res:
                                                                            for s in res:
                                                                                for t in res:
                                                                                    total = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
                                                                                    topTen = sorted(total)
                                                                                    topTenTotal = sum(topTen[10:])
                                                                                    if topTenTotal == 70:
                                                                                        num+=1
                                                                                        if num % 100000==0:print("Num = {}. a = {}. j = {}. o = {}.".format(num,a,j,o))



start()
'''  # <-- lazy equation zzzz.

# [462, 97713, 4772504]

# finds the greatest lowest term for the top ten. top == 70
#   ex: topTen = [-> 1 <-, 1, 1, 1, 6, 12, 12, 12, 12, 12] -> 4(1) + 6 + 5(12) == 70
#   ex: topTen = [-> 7 <-, 7, 7, 7, 7, 7, 7, 7, 7, 7] -> 10(7) == top.
#                   There is no way gLterm can be 8 for these conditions.
def findHighestTerm(res, top):
    #top == 70
    #res == numbers 1 to 12
    #   REQUIRES DEBUGGING. THIS SHIT GARNA' TAKE AWHILE
    #   returns greatest lowest term of 10
    gLowestTerm = 0
    for a in res:
        for b in res:
            for c in res:
                for d in res:
                    for e in res:
                        for f in res:
                            for g in res:
                                for h in res:
                                    for i in res:
                                        for j in res:
                                            listofTerms = [a,b,c,d,e,f,g,h,i,j]
                                            if sum(listofTerms) == top:
                                                lowestTerm = sorted(listofTerms)[0]
                                                if gLowestTerm < lowestTerm:
                                                    gLowestTerm = lowestTerm
    return gLowestTerm # confirms GLowest = 7


# (maxRange of for loop) ** (number of for loops)
def botTenGen(numList, limit):
    numList = numList[:limit]
    numPos = 0
    for a in numList:
        for b in numList:
            for c in numList:
                for d in numList:
                    for e in numList:
                        for f in numList:
                            for g in numList:
                                for h in numList:
                                    for i in numList:
                                        for j in numList:
                                            numPos += 1
    #print(a,b,c,d,e,f,g,h,i,j)
    return numPos


#Only needs to be done once. DONE. refer to dict at top.
def constDictGivenLowest():
    numsBotGen = [1, 2, 3, 4, 5, 6, 7]
    combBotTen = {}
    for limit in numsBotGen:
        combBotTen[limit] = botTenGen(numsBotGen, limit)
    return combBotTen


def outComesWithgLterm1():
    """ when gL = 1, botTen all = 1 and since;
    12,12,12,12,12,6,1,1,1,1 = 6 loops used; it can be repeated to 9 loops for gL = 1
    finds number of possible answers which satisfy:
    botTen = [1, 1, ... , 1] and topTen[:10 - n] = [1, 1, 1, 1, x, x, ... , x]
                                                 = [1, 1, 1, x, x, x, ... , x]
                                                 = [1, 1, x, x, x, x, ... , x]
                                                 = [1, x, x, x, x, x, ... , x]
    """
    total = []
    loops = [6,7,8,9]

    for n in loops:
        total.append(loopFunc(1,12, n))
    return total


def getNumList(rangeMin, rangeMax, nLoops):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    nums = nums[rangeMin - 1:rangeMax]
    numList = []
    for n in range(10, 0, -1):
        if n > nLoops:
            numList.append([1])
        else:
            numList.append(nums)
    return numList


#input range and number of loops: ([1-12], [1-12], [1-10])
def loopFunc(rangeMin, rangeMax, nLoops):
    numList = getNumList(rangeMin, rangeMax, nLoops)
    numPos = 0
    for a in numList[0]:
        for b in numList[1]:
            for c in numList[2]:
                for d in numList[3]:
                    for e in numList[4]:
                        for f in numList[5]:
                            for g in numList[6]:
                                for h in numList[7]:
                                    for i in numList[8]:
                                        for j in numList[9]:
                                            total = sum([a,b,c,d,e,f,g,h,i,j])
                                            if total == 70:
                                                numPos += 1

    return numPos


#wrapper
def run():
    total = []  # list to break up each section.
    gLTotals = []
    combBotTen = {1: 1, 2: 1024, 3: 59049, 4: 1048576, 5: 9765625, 6: 60466176, 7: 282475249}
    gLterm = [1, 2, 3, 4, 5, 6, 7]
    for gL in gLterm:
        if gL == 1:
            total.append(outComesWithgLterm1())
        else:
            tempTotal = loopFunc(gL, 12, 10)
            gLTotals.append([gL, tempTotal])
            total.append(tempTotal * combBotTen[gL])

    return total

run()