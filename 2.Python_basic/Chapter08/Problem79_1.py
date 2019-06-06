#===============================================================================
# counta=0
# countb=0
# a=input()
# b=input()
# for i in a:
#   counta+=1
# for i in b:
#   countb+=1
# print("Larger string is:")
# if counta>countb:
#   print(a)
# else:
#   print(b)
#===============================================================================
count=0
a=input()
for i in a:
  if i.islower():
    count+=1
print(count)