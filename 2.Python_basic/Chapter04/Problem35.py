a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
a.sort()
# aa=list(sorted(a))

### ???안된다구요;;;;;; 다음 이시간에...
b.sort()
print(a)
print(b)
count=0
for count,i in enumerate(a):
    for j in b:
        if a[count]**2==b[count]:
            #print(i,j)
            count+=1
            #print("True")
            
if count==len(a):
    print("True")
else:
    print("False")
        #=======================================================================
        # else:
        #     print("False")
        #=======================================================================
    
def ab(a,b):    
    try:
        return sorted([i**2 for i in a])==sorted(b)
    except ValueError:
        return False