import numpy
import math
def sumnum(n):
    result=0
    nlist=[]
    for i in range(1,n+1):
        result=result+i
        nlist.append(result)
    return nlist   
print(sumnum(50))
#=======================================

a=[i for i in range(1,101) ]
alist=list(numpy.cumsum(a))
print(a)
print(alist)
print(math.gcd(7,21))
