#multiplicationTable(n) =[[1, 2, 3, 4, 5], 
#                         [1, 2, 3, 4, 5], 
#                         [1, 2, 3, 4, 5], 
#                         [1, 2, 3, 4, 5], 
#                         [1, 2, 3, 4, 5]]
def table(n):
    collist=[]
    for j in range(1,n+1):
        rowlist=[]
        for i in range(1,n+1):
            rowlist.append(i)
        collist.append(rowlist)
    return collist
print(table(7))