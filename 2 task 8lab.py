import math
while(True):
    try:
        a = float(input("Enter a:"))
        b = float(input("Enter b:"))
        c = float(input("Enter c:"))
        if a == 0:
            raise ZeroDivisionError("When a = 0, the equation is not quadratic")
        discr = pow(b,2) - 4*a*c
        if discr<0:
            raise ValueError("The discriminant is less than zero, so the equation has no real roots")
        elif discr == 0:
            x = -b / (2*a)
            print("Root value:", "x = ", round(x,2))
            break
        elif discr>0:  
            x1 = (-b + math.sqrt(discr))/(2*a)
            x2 = (-b - math.sqrt(discr))/(2*a)  
            print("Value of the first root:", "x1 =", round(x1,2)) 
            print("Value of the second root:", "x2 =", round(x2,2 ))
            break
    except ZeroDivisionError as g:
        print(f"Errors:{g}.")
        print("You can't divide by zero! Enter another value for a.") 
    except ValueError as e:
        print(f"Error:{e}.")
        print("Error! Enter other values for the variables to get valid roots.")
    except Exception as k:
        print(f"Error: {k}.")
        print("Make sure you enter the correct values and try again.")
