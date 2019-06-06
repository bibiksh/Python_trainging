def count(sting):
    countlist=list(sting)
    #print(countlist)
    return len(countlist)
dog="My dog is potato and She loves potato" 
print(count(dog))
#=================================================def 
def count2(sting):
    countlist=sting.split(" ")
    return (len(countlist))
print(count2(dog))