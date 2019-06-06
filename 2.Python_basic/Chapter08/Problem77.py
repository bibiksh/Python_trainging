nlist="qwertyuiopasdfghjklzxcvbnm"
NLIST="QWERTYUIOPASDFGHJKLZXCVBNM"
n=0
N=0
nN=input()
for i in nN:
    if i in nlist:
        n+=1
    elif i in NLIST:
        N+=1
print("n={},N={}".format(n,N))