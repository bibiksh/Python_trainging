#coding=cp949
sum1=[]
n=int(input())
for i in range(1,n):
    if n%i==0:
        sum1.append(i)
if sum(sum1)==n:
    print("Perfect number O")
    print(sum1)
else:
    print("Perfect number X")
"""
완전수
곱완전수
1,2,3,6
1,2,4,7,14,28
"""
