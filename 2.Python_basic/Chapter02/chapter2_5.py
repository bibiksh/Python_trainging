Korean=int(input("korean=?"))
Math=int(input("Math=?"))
Music=int(input("Music=?"))
avg=(Korean+Math+Music)/3
if avg>=90:
    print("A++")
elif 90>avg>=80:
    print("A+")
elif 80>avg>=70:
    print("A")
else:
    print("F... try again...")