#=======================================================
def rebmun(str):
    return str[::-1]
#=======================================================
def rebmun2(str):
    n=int(str)
    rev=0
    while n>0:
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return rev
#=======================================================
def rebmun3(str):
    numlist=[]
    for number in str:
        numlist.append(number)
    numlist.reverse()        
    return ''.join(numlist)
print(rebmun("326"))         
print(rebmun2("355"))        
print(rebmun3("384"))        
#========================================================