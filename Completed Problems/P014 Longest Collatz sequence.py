

def change(num):
    if num % 2 == 0:
        num = num / 2
    else:
        num = 3*num + 1
    return num

def getTerms(num):
    newCount = 1
    while num != 1:
        num = change(num)
        newCount+=1
    return newCount




def getNumWithGreatestTerms(maxrange):
    n, oldCount = 0, 0

    for num in range(1, maxrange):
        
        newCount = getTerms(num)
        
        if newCount > oldCount: n, oldCount = num, newCount

    return n

gn= getNumWithGreatestTerms
