#coding=cp949
# 1���� n������ �� �� m�� ��� �� ���� ū �� ���ϱ�
def nanugy(n,m):
    emptylist=[]
    for i in range(1,n+1):
        if i%m==0:
            emptylist.append(i)
    return emptylist[-1]
#=================================================

def kkkk(n,m):
    #m=5
    mlist=[i for i in range(1,n+1) if i%m==0]
    return mlist[-1]
print(nanugy(100,3))
print(kkkk(100,3))