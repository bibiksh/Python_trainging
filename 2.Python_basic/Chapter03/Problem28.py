def count(num):
    count=0
    counteven=0
    for i in num:
        
        # i.isalpaha  i.isdigit
        if i in "0123456789":
            count+=1
            if int(i)%2==0:
                counteven+=1
    return count,counteven
b="223422223a444888s"
print(count(b))