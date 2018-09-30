import math
import sys
def calculator():
    a=int(input("Enter the number a:"))
    b= int(input("Enter the number b:"))
    operation=int(input("Enter the operation: 1-add,2-sub,3-multiply,4-divide,5-exit"))
    if operation==1:
        print(a+b)
    elif operation==2:
        print (a-b)
    elif operation==3:
        print (a*b)
    elif operation==4:
        print (a/b)
    elif operation==5:
         sys.exit()
calculator()
