#coding=cp949
"""
����
����
���
�ǰ�
�Ǳ�
�ñ�
"""
nlist=[]
nlist2=[]
def nn(n):
    for i in range(len(n)):
        if i%2==0:
            nlist.append(n[i])
    return "".join(nlist)
#========================================
def nn2(n2):
    for i,v in enumerate(n2):
        if i%2==0:
            nlist2.append(v)
    return "".join(nlist2)
#========================================
n=input()
n2=input()
print(nn(n))
print(nn2(n2))