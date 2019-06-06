#coding=cp949
def hello(n):
    word="hello"
    index=0
    for i in range(len(n)):
        if index==5:
            return "Yes"
        
        if n[i]==word[index]:
            index+=1
    if index<5:
        return "No"
    else:
        return "Yes"
    
m=input()
print(hello(m))