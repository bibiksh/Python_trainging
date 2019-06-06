a=input()
b=a.count("(")
c=a.count(")")
if b==c:
    print("good")
elif c>b:
    print("bad")    
else:
    print(b-c)
