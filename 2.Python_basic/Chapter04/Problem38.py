def difflist(a,b):
    emptylist=[]
    for i in a:
        if i not in b:
            emptylist.append(i)
    return emptylist
a=[3,4,5,6,7]
b=[4,5,8,9,10]
print(difflist(a,b))