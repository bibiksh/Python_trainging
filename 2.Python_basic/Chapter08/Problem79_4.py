a=input()
lower=0
upper=0
for i in a:
  if i.islower():
    lower+=1
  if i.isupper():
    upper+=1
print("The number of lowercase characters is:")
print(lower)
print("The number of uppercase characters is:")
print(upper)