#1+x**2/2+x**3/3.......
sumnum=1
n=int(input())
x=int(input())

for i in range(2,n+1):
    sumnum+=x**i/i
print(sumnum)