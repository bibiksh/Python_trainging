def bearbear(l,b):
    count=0
    while l<=b:
        l=l*3
        b=b*2
        count+=1
    return count
print(bearbear(4,7))