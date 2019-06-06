#a,b,c : start a b end c divisor
def divisor(a,b,c):
    dlist=[]
    for i in range(a,b+1):
        if i%c==0:
            dlist.append(i)
    return dlist[-1]
print(divisor(1,100,13))
#lambda=========================================
divisor2=lambda a,b,c:b-b%c
print(divisor2(1,100,13))