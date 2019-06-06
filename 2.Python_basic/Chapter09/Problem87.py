nlist=list(map(int,input().split()))
for i in range(len(nlist)):
    for j in range(len(nlist)-1-i):
        if nlist[j]>nlist[j+1]:
            nlist[j],nlist[j+1]=nlist[j+1],nlist[j]
print(nlist)