#coding=cp949
num1=input()
alist=list(num1)  # 153 
n=int(alist[0])
u=int(alist[1])
m=int(alist[2])
sum1=n**3+u**3+m**3   # pow(n,3)
if int(num1)==sum1:
    print("Amstrong Number")
else:
    print("Not Amstrong Number")
#============================================================
empty=[]
for i in range(100,1000):
    #ilist=list(i)
    I1=int(str(i)[0])
    I2=int(str(i)[1])
    I3=int(str(i)[2])
    sum1=I1**3+I2**3+I3**3
    if i==sum1:
        empty.append(i)
print(empty)