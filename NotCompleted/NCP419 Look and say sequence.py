'''
The look and say sequence goes
1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...
The sequence starts with 1 and all other members are obtained
by describing the previous member in terms of consecutive digits.
It helps to do this out loud:
1 is 'one one'  11
11 is 'two ones'  21
21 is 'one two and one one'  1211 
1211 is 'one one, one two and two ones'  111221
111221 is 'three ones, two twos and one one'  312211
...
numDict = {1: 11, 11: 21, 111:31, 2: 12, 22: 22, 222:32, 3: 13, 33: 23, 333:33}
#break input number into "new numbers"
#	when number changes, put into key.
#		11231 -> 11, 2, 3, 1


Define A(n), B(n) and C(n) as the number of ones, twos and threes
in the n'th element of the sequence respectively.
One can verify that A(40) = 31254, B(40) = 20259 and C(40) = 11625.

Find A(n), B(n) and C(n) for n = 1012.
Give your answer modulo 230 and separate your values for A, B and C by a comma.
E.g. for n = 40 the answer would be 31254,20259,11625
'''

#count how many of same before next char changes.
# y   is         13112221:
#       1   3   1   1   2   2   2   1
#x =    1   1   *   2   *   *   3   1
#n =    1   3   #   1   #   #   2   1
#newy is         1113213211

#x: 11231
#n: 13121

#newy  = xn xn xn xn xn
#      = 11 13 21 32 11
#      = 1113213211
#newy is 1113213211 <3


#finds x
def countY(listY):
    countX=[]
    n = 0
    #while len > 1, count multiple
    while len(listY) > 1:
        n=0
        while len(listY) > 2: #error here.
            while listY[0] == listY[1]:
                n+=1
                listY=listY[1:]
            n+=1
            listY=listY[1:]
            countX.append(str(n))
    #if only 1 element left, append 1
    if len(listY)==1:return countX.append('1')
    print(countX)

#for finding x, try going through input string. for length of string
    #if the old term is equal to the old term. count and move on.
    #if the old term is different, add count to list
    #if the leng is equal to 1, do previous two steps but end afterwards
        
#convert y to n
#           
#for finding n, try going through input string. for length of string
    #if the new term is equal to the old term. do nothing and move on.
    #if the new term is different, add old term to list
    #if the leng is equal to 1, do previous two steps but end afterwards
#for finding n, try going through input string. for length of string
    #if the term in question is new, add to list.
    #if the next term is the same as previous, move on
    #if the leng is equal to 1, do previous two steps but end afterwards
#compress list. remove duplicates. 111321 -> 1321
#
        
def getNextY(y):
    y = list(y)
    count(y)



#y='13112221'
u='1113213211'
#countY(y)
countY(u)

#expecting n = [11231]
#expecting n = [3111112]
