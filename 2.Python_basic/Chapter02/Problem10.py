def strings(a,b):
    if len(a)<len(b):
        return "a is small."
    if len(a)>len(b):
        return "a is big."
    if a<b:
        return "a is small."
    if a>b:
        return "a is big."
    if abs(int(a))<abs(int(b)):
        return "...?"
    return "a=b"
    
    
print(strings("33","444")) 
print(strings("875","799"))