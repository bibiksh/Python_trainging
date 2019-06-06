#a e i o u
a="i love dog"
print(a.upper())
b="I LOVE DOG"
print(b.lower())
print(a.capitalize())
alist=a.split()
#print(alist)
aalist=[]
for i in alist:
    aalist.append(i.capitalize())
   
astring=" ".join(aalist) 
print(astring)
