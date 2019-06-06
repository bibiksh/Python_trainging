def dagaghyoung(n):
    if 360%(180-n)==0:
        return "yes"
    else:
        return "no"
n=int(input())
alist=[]
for i in range(n):
    m=int(input())
    alist.append(m)
    
for i in alist:
    print(dagaghyoung(i))