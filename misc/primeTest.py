
import listPrimes


primeList = listPrimes.returnList()

def sumUnderX(inputList, num):
    sumOf = 0
    for ix in range(len(inputList)):
        if int(inputList[ix]) <= num:
            sumOf += int(inputList[ix])
        else:
            break
    return sumOf

#test