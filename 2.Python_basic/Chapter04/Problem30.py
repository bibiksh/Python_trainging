def num(number):
    for i in range(1,number+1):
        if i%2!=0 and i%3!=0:
            print(i)
#num(20)
#=========================================
def ssum(number):
    numsum=0
    for i in range(1,number+1):
        numsum+=i
    return numsum
print(ssum(10))
#==========================================
def sssum(number):
    numlist=[]
    for i in range(1,number+1):
        numlist.append(i)
    return sum(numlist)
print(sssum(11))
#==========================================