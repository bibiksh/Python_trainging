def num(n):
#    k=0
    for i in range(2,n):
       if n%i==0:
#           k+=1
           return "not prime"
    return "prime"
print(num(35))

#    if k<=0:
        