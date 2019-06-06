import timeit

a=[12, 30, 16, 11, 51, 1, 44, 85, 19, 5, 22, 71, 29, 40, 42, 88]
def bubble(a):
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
def bubble2(ab):
    ab.sort()
    return ab
print(bubble(a))
print(bubble2(a))
# Approach 1: Execution time 
print(timeit.timeit('bubble(a)', globals=globals(), number=10000))
# Approach 2: Execution time
print(timeit.timeit('bubble2(a)', globals=globals(), number=10000))