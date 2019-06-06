#https://codeforces.com/problemset/problem/71/A
n=int(input())
nlist=[]
for i in range(n):
    m=input()
    nlist.append(m)
#print(nlist)
blist=[]
for i in nlist:
    #print(i)
    if len(i)>10:
        i=i[0]+str(len(i)-2)+i[-1]
        #print(i)
    blist.append(i)
for i in blist:
    print(i)     
"""   
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
"""