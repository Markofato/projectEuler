res = [1,2,3,4,5,6]

def start():
    num = 0
    for a in res:
        for b in res:
            for c in res:
                for d in res:
                    for e in res:
                        total = [a,b,c,d,e]
                        num+=1
                        if num % 1000 == 0: print("Num = {}. a = {}. b = {}. c = {}.".format(num,a,b,c))
                        #print(total)
                        #topThree = sorted(total)
                        #print(topThree[2:])
                        #topThreeTotal = sum(topThree[2:])
                        #print(topThreeTotal)
                        #if topThreeTotal == 15:
                            #num+=1
                            #print("Num = {}. a = {}. b = {}. c = {}.".format(num,a,b,c))
    return num
