ilist=[]
n=int(input())
for i in range(n):
    m=input()
    ilist.append(m)
for j in ilist:
    if j==j[::-1]:
        print("0")
    if len(j)%2!=0:
        for k in j:
            newstr=""
            newstr=j.replace(k,"")
            if newstr==newstr[::-1]:
                print("1")
                break
    if len(j)%2==0 and j!=j[::-1]:
        print("2")