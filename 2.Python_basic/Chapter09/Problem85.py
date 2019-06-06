m=input()
nlist=""
for i in range(len(m)):
  if m[i].isupper():
    nlist+=m[i].lower()
  if m[i].islower():
    nlist+=m[i].upper()
print(nlist)