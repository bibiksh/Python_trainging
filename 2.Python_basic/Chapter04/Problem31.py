def ssum(number):
    numlist=[]
    numsum=0
    for i in range(1,number+1):
        numsum+=i
        numlist.append(numsum)
    #return numlist[-1]
    return numlist
print(ssum(12))
#=======================================
a=[i for i in range(1,12) if i%2==0]
print(a)