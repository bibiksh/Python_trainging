#coding=cp949
def nemo(n):
    for j in range(n):
        for i in range(n):
            if j==i:
                print("1",sep=" ",end=" ")  # seperate separate
            else:
                print("0",sep=" ",end=" ")
        print()
nemo(4)
"""
����
�ӻ�
����
�̻�
����
�ǻ�
�̻�
"""
def nemo2(n):
    total=[]
    for i in range(n):
        sublist=[]
        for j in range(n):
            if i==j:
                sublist.append(1)
            else:
                sublist.append(0)
                
        total.append(sublist)
    return total
print(nemo2(4))
