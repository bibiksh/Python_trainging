#===============================================================================
# n=int(input())
# if n%2==0:
#     m=n//2
#     print("{} {}".format(m,m))
# else:
#     j=n//2
#     i=j+1
#     print("{} {}".format(i,j))
#===============================================================================
#===============================================================================
# n=int(input())
# nlist=list(map(int,input().split()))
# for i in range(len(nlist)):
#     for j in range(len(nlist)-1-i):
#         if nlist[j]>nlist[j+1]:
#             nlist[j],nlist[j+1]=nlist[j+1],nlist[j]
# print(nlist[-2])
#===============================================================================
#===============================================================================
blist=[]
m=int(input())
mlist=list(map(int,input().split()))
#mlist=input().split()
mlist.sort()
mm=mlist[-2]
print(mm)
for i in mlist:
    blist.append(str(i))
print(" ".join(blist))