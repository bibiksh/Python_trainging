#[[1,2,3],[2,4,6],[3,6,9]]
alist=[]

for i in range(1,4):
    asub=[]
    for j in range(1,4):
        asub.append(i*j)  
    alist.append(asub)
print(alist)