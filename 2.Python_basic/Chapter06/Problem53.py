#coding=cp949
"""
A*B=G*L
"""

a=10
#auto aa =10;
A=int(input())
B=int(input())
if A>B:
    minimum1=A
else:
    minimum1=B
while True:
    if minimum1%A==0 and minimum1%B==0:
        print(minimum1)
        break
    minimum1+=1
#=====================================================
import math
print(math.gcd(60,48))
#=====================================================
def LCM(A,B):
    return A*B//(math.gcd(A,B))
print(LCM(A,B))
## Using Euclidean Algorithm