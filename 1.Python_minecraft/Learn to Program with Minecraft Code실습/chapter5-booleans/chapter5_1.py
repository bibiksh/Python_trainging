#===============================================================================
# print(1/0)
#===============================================================================

try:
    a=int( input("input your first number:"))
    b=int( input("input your second number:"))
    print(a/b)

except: 
    print("zero error...")
#===============================================================================
# except ZeroDivisionError :
#     print("zero error...")    
#===============================================================================
    