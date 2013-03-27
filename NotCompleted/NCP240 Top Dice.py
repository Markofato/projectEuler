res = [1,2,3,4,5,6,7,8,9,10,11,12]

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
'''

# find where top 10 == 70. for each grab bot term and put trough dict

def botTenGen(res, n):
    numPos = 0
    res = res[:n]
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
                                            numPos += 1
    return numPos

# n = topList[0]

def constDictGivenLowest(res, n):
    posLower = {}
    res = res[:n]
    for limit in res:
        posLower[limit] = botTenGen(res, limit)
    return posLower

print(constDictGivenLowest(res, 3))
#print(botTenGen(res, 3))