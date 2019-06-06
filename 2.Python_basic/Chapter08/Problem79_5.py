#The quick brown fox jumps over the lazy dog
alist="qwertyuiopasdfghjklzxcvbnm"
blist=[]
a=input().split()
#print(a)
for i in a:
    for j in i.lower():
        #print(j)
        if j in alist:
            blist.append(j)
#print(blist)
clist=list(set(blist))
if len(clist)==26:
    print("The string is a pangram")
else:
    print("The string isn't a pangram")