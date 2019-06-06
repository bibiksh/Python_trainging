n=int(input())
rlist=[]
count=0
for i in range(n):
    r=int(input())
    rlist.append(r)
q=int(input())
for i in rlist:
    if i==q:
        count+=1
if count==0:
    print("Bad")
elif count==1:
    print("Not bad")
else:
    print("Wow!!!")