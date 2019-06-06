print("1=egg")
print("2=pancake")
print("3=potato")
print("4=sweet potato")
print("")
breakfast=int(input("Chose your breakfast : "))
if breakfast==1:
    print("1=The eggs are not all ripe.")
    print("2=The eggs are all ripe.")
    print("")
    chose=int(input("Chose your breakfast : "))
    if chose==1:
        print("The eggs are not all ripe.")
    elif chose==2:
        print("The eggs are not all ripe.")
else:
    print("Sorry, I do not have the ingredients.")