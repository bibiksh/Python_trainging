nm=[]
n,m=map(int,input().split())
for i in range(1,n+1):
  nm.append(i)
for j in range(1,m+1):
  nm.append(j)
nm.sort()
print(nm)