def sumnum(alist):
    total=0
    for i in alist:
        total+=i/100
        
    #return (total/len(alist))*100
    return "{0:.12f}".format((total/len(alist))*100)  # printf("%.4f " ,a)  print("%.4f" %(a))
n=int(input())
alist=list(map(int,input().split()))
print(sumnum(alist))