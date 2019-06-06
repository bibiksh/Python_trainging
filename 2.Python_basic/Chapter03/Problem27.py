def num(num,n):
    count=0
    numstr=str(num)
    for i in numstr:
        if int(i)==n:
            count+=1
    return count
a=1234533344444
b="223422223a444888s"
n=3
print(num(a,n))
#===========================================
def num2(num,n):
    numstr=str(num)
    count2=numstr.count("3")
    return count2
print(num2(a,n))
#===========================================
def num3(num):
    numstr=str(num)
    count3=0
    for i in numstr:
        if int(i)%2==0:
            count3+=1
    return count3
print(num3(a))
#===========================================

print(num4(b))
     