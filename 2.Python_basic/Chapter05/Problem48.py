#coding=cp949
"""
(^-^)7
"""
def zerone(a):
    count=0
    for i in range(len(a)):
        if a[i]=="0":
            count+=1
    onecount=len(a)-count
    return abs(onecount-count)
    #return abs(len(a)-count*2)
n=int(input())
m=input()
print(zerone(m))