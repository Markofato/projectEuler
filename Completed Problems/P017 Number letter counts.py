'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
#break up into XYZ
#f1(X) has ( for Y loop ) f2(Y) inside
#f2(Y) has ( for Z loop ) f3(Z) inside
#f3(Z)
for X in number:
    for Y in number:
        for Z in number:
            #num = []
            #num += X + Y + Z
            num = funcAppendXYZ(X,Y,Z) #has conditions
            name = funcGenName(num) #has conditions
            numList += [num, name]
#add on '1000'
#for f1(x), f2(y), f3(z) - have conditions and sister functions for conditions
#conditions for Y before ( for Z loop ) or after.
#conditions for X before ( for Y loop ) or after. - compare complexities.
#converts num into number of letters
def convert(num):

X
1='One'
2='Two'
3='Three'
4='Four'
5='Five'
6='Six'
7='Seven'
8='Eight'
9='Nine'

Y
10='Ten'
11='Eleven'
12='Twelve'
13='Thirteen'
14='Fourteen'
15='Fifteen'
16='Sixteen'
17='Seventeen'
18='Eighteen'
19='Nineteen'
20='Twenty'

21	Twenty-one	long score[1]
22	Twenty-two	Deuce-deuce
23	Twenty-three
24	Twenty-four	two dozen
25	Twenty-five
26	Twenty-six
27	Twenty-seven
28	Twenty-eight
29	Twenty-nine
30	Thirty
31	Thirty-one
40	Forty
50	Fifty	half-century
60	Sixty	three-score
70	Seventy	three-score and ten
80	Eighty	four-score
87	Eighty-seven	four-score and seven
90	Ninety
100	One hundred	centred, century, ton, short hundred
101	One hundred [and] one
110	One hundred [and] ten
111	One hundred [and] eleven
120	One hundred [and] twenty	long hundred,[1] great hundred, (obsolete) hundred
121	One hundred [and] twenty-one
144	One hundred [and] forty-four	gross, dozen dozen, small gross
169	One hundred [and] sixty-nine	baker's gross[citation needed]
200	Two hundred
300	Three hundred
666	Six Hundred [and] sixty-six	Number of the Beast
1 000	One thousand
'''
#21124! <3

X = {'0':'','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}

Y = {'0':'','1':'Ten','2':'Twenty','3':'Thirty','4':'Forty','5':'Fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety'}

YX = {'0':'Ten','1':'Eleven','2':'Twelve','3':'Thirteen','4':'Fourteen','5':'Fifteen','6':'Sixteen','7':'Seventeen','8':'Eighteen','9':'Nineteen'}  #,'20':'Twenty'}

Z = {'0':'','1':'Onehundred','2':'Twohundred','3':'Threehundred','4':'Fourhundred','5':'Fivehundred','6':'Sixhundred','7':'Sevenhundred','8':'Eighthundred','9':'Ninehundred'}


numbers = ['0','1','2','3','4','5','6','7','8','9']


def startOne():
    total = 0
    for z in numbers:
        for y in numbers:
            for x in numbers:
                numWord = []
                if y == '1':
                    numWord += Z[z] + YX[x]
                    #print(''.join(numWord))
                else:
                    numWord += Z[z] + Y[y] + X[x]
                    #print(''.join(numWord))
                if z > '0' and y != '0' or z > '0' and x != '0':
                    numWord += 'and'
                total += len(numWord)
                #print(''.join(numWord))
    total += len('onethousand')
    return total


print(startOne())
print(sum([len(X[x]) for x in numbers[:6]]))