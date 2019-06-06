n=int(input())
#===============================================================================
# alist=list(map(str,input().split()))
# blist=list(map(int,input().split()))
#===============================================================================
#===============================================================================
# clist=[]
# #for i in range(n):
# m=zip(alist,blist)
# clist.append(list(m))
# print(clist)
#===============================================================================
a=[[i,j] for i,j in zip(input().split() ,map(int,input().split()))]
#print(a)
for i in range(len(a)):
    for j in range(0,len(a)-1-i):
        if a[j][1]>a[j+1][1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)