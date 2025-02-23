def add(a,b):
    c=a+b
    print(f"Addition of {a} and {b} is:{c}")
    return c    
def sub(a,b):
    c=a-b
    print(f"Subtraction of {a} and {b} is:{c}")
    return c    
def mul(a,b):
    c=a*b
    print(f"Multiplication of {a} and {b} is:{c}")
    return c    
def div(a,b):
    c=a/b
    print(f"Division of {a} and {b} is:{c }")
    return c    
def mod(a,b):
    c=a%b
    print(f"Modulus of {a} and {b} is:{c}")
    return c

while True:
    print("\nMenu:")
    print("1 for addition.")    
    print("2 for subtraction.")
    print("3 for multiplication.")
    print("4 for division.")
    print("5 for modulus.")
    print("6 for exiting program.")
    choice=int(input("Enter your choice:"))
    if choice==6:
        print("You are now exited from program.")
        break
    
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    
    if choice==1:
        add(num1,num2)
    elif choice==2:
        sub(num1,num2)    
    elif choice==3:
        mul(num1,num2)
    elif choice==4:
        div(num1,num2)
    elif choice==5:
        mod(num1,num2)            
    else:
        print("Enter the valid choice.")    