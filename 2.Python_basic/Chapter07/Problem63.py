n=int(input())
sumnum=0
for i in range(1,n+1):
    sumnum+=1/i
print(sumnum)

print(sum([1/i for i in range(1,n+1)]))