def prob1(a,b,cap):
    result = 0
    n,m,z = 1,1,1
#    print (n,m,z)
    while a*n < cap:
        result += a*n
        n += 1
#        print (result)
    while b*m < cap:
        result += b*m
        m += 1
#        print (result)
    while a*b*z < cap:
        result -= a*b*z
        z += 1
#        print (result)
    return result
print (prob1(3,5,1000))



