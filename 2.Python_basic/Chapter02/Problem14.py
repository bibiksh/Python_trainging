def capitalize(str):
    words=str.split(" ")
    result=[]
    for word in words:
        #word.capitalize()
        #result.append(word)
        result.append(word.capitalize())
    return ' '.join(result) 
potato="i love potato"
print(potato)
print(capitalize(potato))