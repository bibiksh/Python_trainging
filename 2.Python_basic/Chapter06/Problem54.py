#coding=cp949
"""
100가지 리스트:
    for :
    while :
"""
import timeit
def make_count(n):
    count=1
    nlist=[]
    while count<n:
        nlist.append(count)
        count+=1
    return nlist
def make_count2(n):
    ilist=[]
    for i in range(1,n):
        ilist.append(i)
    return ilist
print(make_count(100))
print(make_count2(100))
print(timeit.timeit('make_count(500)', globals=globals(), number=10000))
print(timeit.timeit('make_count2(500)', globals=globals(), number=10000))