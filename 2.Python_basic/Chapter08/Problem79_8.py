count=0
a=input().split()
word=input()
for i in a:
  if i==word:
    count+=1
print("Count of the word is:")
print(count)