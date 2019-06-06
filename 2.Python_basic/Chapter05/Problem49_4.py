b=[-45,-23,56,23,7,0]
def sumnum(b):
    evlist=[]
    olist=[]
    mlist=[]
    errorlist=[]
    # e,o,m=[],[],[]
    for i in b:
        if i>0:
            if i%2==0:
                evlist.append(i)
            else:
                olist.append(i)
        if i<0:
            mlist.append(i)
        elif i==0:
            errorlist.append(i)
    return evlist,olist,mlist,errorlist
print(sumnum(b))
#a,b,c,d=