count=0
nlist=list(map(int,input().split()))
mlist=list(map(int,input().split()))
for i in nlist:
  if i in mlist:
    count+=1
if count==0:
    print("false")
else:
    print("true")