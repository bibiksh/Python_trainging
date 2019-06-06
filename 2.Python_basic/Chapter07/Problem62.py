alist=list(map(int,input().split("+")))
alist.sort()
blist=[]
for i in alist:
    blist.append(str(i))
print("+".join(blist))