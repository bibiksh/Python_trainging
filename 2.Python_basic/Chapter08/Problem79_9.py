count=0
a=input().split()
word=input()
for i in a:
    #print(i)
    if i==word:
        print("Substring in string!")
        count+=1
if count==0:
    print("Substring not found in string!")