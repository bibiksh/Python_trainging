import random
from test.test_buffer import rand_aligned_slices
def ranndom(number):
    emptylist=[]
    for i in range(number):
        emptylist.append(random.randint(1,24))
    return emptylist

print(len(ranndom(10)))
print(ranndom(10))
#======================================================
b=ranndom(10)
print(b)
temp=b[0]
b[0]=b[9]
b[9]=temp
print(b)


a=[2,2,5,3,4,3,6]
print(a)
b=set(a)
print(list(b))