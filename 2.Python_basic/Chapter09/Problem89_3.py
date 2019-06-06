mlist=[]
n=int(input())
for i in range(n):
    m=input()
    mlist.append(m)
mlist.sort(key=len)
#===============================================================================
# for i in range(len(mlist)):
#     for j in range(len(mlist)-1-i):
#         if len(mlist[j])>len(mlist[j+1]):
#             mlist[j],mlist[j+1]=mlist[j+1],mlist[j]
#===============================================================================
print(mlist)