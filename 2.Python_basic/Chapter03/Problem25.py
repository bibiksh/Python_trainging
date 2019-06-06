#a e i o u
def vowel_count(sting):
    count=0
    for i in range(len(sting)):
        if sting[i].lower() in "aeiou":
            count+=1
    return count
a="i love potato"
print(vowel_count(a))