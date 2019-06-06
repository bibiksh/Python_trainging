digit=0
alpha=0
a=input()
for i in a:
  if i.isdigit():
    digit+=1
print("The number of digits is:")
print(digit)
print("The number of characters is:")
print(len(a))