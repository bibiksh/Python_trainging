#===============================================================================
# ablist=[]
# n,m=map(int,input().split())
# alist=list(map(int,input().split()))
# blist=list(map(int,input().split()))
# for i in alist:
#     for j in blist:
#         if i==j:
#             ablist.append(j)
# ablist.sort()
# print(ablist)
#===============================================================================
#===============================================al

alist=[1,2, 3]
blist=[3,4,5]
clist=list(set(alist) & set(blist))
print(clist)