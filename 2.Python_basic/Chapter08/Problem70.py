#break continue
def strring(sting):
    #return sting[-1:]+sting[1:-1]+sting[:1]
    return sting[-1]+sting[1:-1]+sting[0]
n=input()
print(strring(n))