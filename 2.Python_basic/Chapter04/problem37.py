#coding=cp949
def pr(number):
    emptylist=[]
    for i in range(2,number):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            emptylist.append(i)
    return len(emptylist)
print(pr(100))
#===============================================================================
# n=int(input("Enter upper limit of range: "))
# sieve=set(range(2,n+1))
# while sieve:
#     prime=min(sieve)
#     print(prime,end="굏")
#     sieve-=set(range(prime,n+1,prime))
#  
# print()
#===============================================================================