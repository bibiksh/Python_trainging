#1
for i in range(5):
    print("*",end='')
#2
for j in range(4):
    for i in range(5):
        print("*",end="")
    print("")
#3
for j in range(5):
    for i in range(j+1):
        print("*",end="")
    print("")


#4 
for j in range(5):
    for i in range(5-j):
        print("*",end="")
    print("")
#5
for j in range(5):
    for i in range(4-j):
        print(" ",end="")
    for i in range(j+1):
        print("*",end="")
    print("")

#6
for j in range(5):
    for i in range(j):
        print(" ",end="")
    for i in range(5-j):
        print("*",end="")
    print("")

#7
for j in range(5):
    for i in range(4-j):
        print(" ",end="")
    for i in range(2*(j+1)-1):
        print("*",end="")
    print("")
#8
for j in range(5):
    for i in range(j):
            print(' ', end='')
    for i in range(2*(5-j)-1):
            print('*', end='')
    print("")

#9

apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 302, 303], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]
for floor in apart:
    for house in floor:
            if house in arrears:
                continue
            else:
                print("Newspaper delivery: ", house)
##### start print

import math
#s=["  *  "," ** ","*****"]
s = ['  *   ',' * *  ','***** ']

def makestar(shift):
    c=len(s)
    for i in range(c):
        s.append(s[i]+s[i])
        s[i]=' '*shift+s[i]+' '*shift 
n=int(input())
k=int(math.log(n/3,2))

for i in range(k):
    makestar(int(pow(2,i)*3))

for i in range(n):
    print(s[i])
