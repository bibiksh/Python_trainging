#coding=cp949
"""
����
���
�ñ�
���
����
���
"""
#from itertools import count
def sum_mer(n):
    count=1
    sumnum=0
    while sumnum<=n:
        sumnum=sumnum+count
        count+=1
    return count-2
def sum_mer2(n):
    alist=[]
    sumnum=0
    for i in range(100):
        sumnum+=i
        if sumnum<=n:
            alist.append(i)
    return alist[-1]
print(sum_mer(14))
print(sum_mer2(100))
#===============================================================================
# �󸮽�Ʈ=>emptylist,beanlist
# �Լ�=>hamsu
#===============================================================================
