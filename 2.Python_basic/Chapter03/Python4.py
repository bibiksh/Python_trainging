alist=[]
for i in range(5):
    a=input()
    alist.append(a)
A=alist.count("A")
B=alist.count("B")
if A>B:
    print("A")
else:
    print("B")