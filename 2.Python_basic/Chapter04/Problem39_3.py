def jipp(jlist):
    oddlist=[]
    elist=[]
    for j in jlist:
        if j%2==0:
            elist.append(j)
        else:
            oddlist.append(j)
    clist=[a for a in zip(elist,oddlist)]
#     for i in range(len(elist)):
#         a=zip(elist,oddlist)
#         clist.append(a)
#     return clist
    return clist
jlist=[1,2,3,4,5,6]
print(jipp(jlist))
#return [val for item in [a for a in zip([e for i, e in enumerate(athletes) if i % 2 != 0], [e for i, e in enumerate(athletes) if i % 2 == 0])] for val in item]
alist=[i for i in range(100)]
print(alist)