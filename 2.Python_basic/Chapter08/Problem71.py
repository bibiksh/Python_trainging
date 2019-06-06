count=0
count2=0
n=input()
for i in n:
    if i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
        count+=1
print(count)
#============================================================================================================
a="aeiouAEIOU"
for i in n:
    if i in a:
        count2+=1
print(count2)