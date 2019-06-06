def dono(m,n):
    bordd=m*n
    donoo=2
    return bordd//donoo
alist=list(map(int,input().split()))
m=alist[0]
n=alist[1]
print(dono(m,n))