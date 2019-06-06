def soup(strring):
    alist=list(strring)
    print(alist)
    #alist=strring.split(" ")
    alist.sort()
    return "".join(alist)
print(soup("potato"))
#==================================================
def soup2(ing,str1):
    strlist=list(ing)
    result=0
    for count,str in enumerate(strlist):
        if str==str1:
            result=count+1
    return result
print(soup2("potato","a"))