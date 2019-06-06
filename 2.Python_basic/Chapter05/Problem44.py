#coding=cp949
def settin(n):
    alist=[]
    #strn=list(str(n))
    strn=str(n)
    for i in strn:
        alist.append(i)
    nlist=set(alist)
    if len(nlist)==1:
        return True
    else:
        return False
print(settin(1111))