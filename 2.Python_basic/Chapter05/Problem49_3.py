#coding=cp949
#===============================================================================
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70
#===============================================================================
n=int(input())
for i in range(1,11):
    #print("{}{}{}{}{}".format(n,"x",i,"=",n*i))
    print("{} x {} = {}".format(n,i,n*i))
    
#format
a="test"
b="test2"
print("{0} {0} {1} {1}".format(a,b))