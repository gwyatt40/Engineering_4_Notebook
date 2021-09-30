# Quadratic Calculator

# Written by Georgia Wyatt

# 9.20.21


# import complex math module (contains sqrt)
import cmath

print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c = 0")

 # while True loop to repeat actions
while True: 
    a = int(input("Enter a: ")) # input coefficients
    b = int(input("Enter b: ")) 
    c = int(input("Enter c: "))

    # calculate the discriminant
    d = (b**2) - (4*a*c)


    if d >= 0: # positive or 0 discriminant means two real roots
        sol1 = (-b-cmath.sqrt(d))/(2*a) # calculate roots (quadratic formula)
        sol2 = (-b+cmath.sqrt(d))/(2*a)
        print('The solutions are {0} and {1}'.format(sol1,sol2))
    
    if d < 0: # negative discriminant means no real roots
        print("No real roots")
        
   # exit code
    print("Press enter to continue")
    print("Press x to exit")
    
    x = input("")
       
    if x:
       print("Goodbye!")  
       break 
        
