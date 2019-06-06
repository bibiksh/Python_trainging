n=int(input())
#print(bin(n))
"""
bin
"""
#print(bin(n)[2::])
nlist=[]
mlist=[]
for i in range(n+1):
    ii=bin(i)[2::]
    nlist.append(ii)
#print(nlist)

for i in range(n+1):
    if len(bin(i)[2::])<len(bin(n)[2::]):
        mlist.append("0"*(len(bin(n)[2::])-len(bin(i)[2::]))+bin(i)[2::])    
    else:
        mlist.append(bin(i)[2::])
print(mlist)