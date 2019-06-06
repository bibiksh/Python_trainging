alist=[]
for i in range(5):
    a=int(input("input:"))
    alist.append(a)
#alist.sort()
#Maxnum=alist[-1]
maxnum=max(alist)
if 0<=maxnum<30:
    print("good")
elif 30<=maxnum<80:
    print("normal")
elif 80<=maxnum<150:
    print("bad")    
elif 150<=maxnum:
    print("serious")