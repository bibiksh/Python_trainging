def h(n):
    if n>1:
        h(n//2)
        
    print(n%2,end="")
h(100)