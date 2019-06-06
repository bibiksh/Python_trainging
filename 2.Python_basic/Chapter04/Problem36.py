#coding=cp949
def yearcal(n):   # string n     
    alist=[i for i in range(int(n)+1,10000)]
    blist=[]
    for i in range(1,10000):
        blist.append(i)
    for a in alist:
        if len(set(str(a)))==4:
            return a
year=input()
print(yearcal(year))
"""
list
"""