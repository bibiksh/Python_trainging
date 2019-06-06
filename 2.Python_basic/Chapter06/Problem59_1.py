#coding=cp949
a=int(input())
b=int(input())
c=int(input())
if a<=0 or b<=0 or c<=0:
    print("error")
else:
    if a==b==c:  # a==b and b==c and c==a
        print("jung")
    elif a==b or b==c or c==a:
            print("Edngbouyn")
    else:
        print("budngbouyn")