ilist=[]
n=int(input())
for i in range(n):
    m=int(input())
    ilist.append(m)
ilist.reverse()
blist=[ilist[0]]
maxnum=ilist[0]
for i in ilist:
    if i>ilist[0]:
        if i>maxnum:
            maxnum=i
            blist.append(i)
#print(blist)
print(len(blist))