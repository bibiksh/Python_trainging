#coding=cp949
#a b c
#if a<b<c? => True,False
a=7
b=5
c=3
def is_in_ragne(a,b,c):
    if a<b<c:
        return True
    else:
        return False
# different way
def is_in_ragne2(a,b,c):
    if a<c:
        if a<b<c:
            return True
        else:
            return False
    else:
        if c<b<a:
            return True
        else:
            return False

# different way
def is_in_ragne3(a,b,c):
    if a<c:
        for i in range(a,c+1):
            if i==b:
                return True
        return False 
    else:
        for i in range(c,a+1):
            if i==b:
                return True
        return False 

print(is_in_ragne(a,b,c))
print(is_in_ragne2(a,b,c))
print(is_in_ragne3(a,b,c))