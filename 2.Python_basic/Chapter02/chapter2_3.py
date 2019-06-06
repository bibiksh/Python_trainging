#quotient remainder => 
a=int(input("a=? : "))
b=int(input("b=? : "))
quotient=a//b
remainder=a%b
aa=int(input("a//b=? : "))
bb=int(input("a%b=? : "))
if quotient==aa:
    print("You win.")
else:
    print("you lose...hahaha")
if remainder==bb:
    print("You win.")
else:
    print("You lose...hahaha")
print("Quotient : {},Remainder : {}".format(quotient,remainder))
print(f"{quotient},{remainder}")