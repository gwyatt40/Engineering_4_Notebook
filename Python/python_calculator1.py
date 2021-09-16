# Python Program 01 - Calculator (ENGR4)

#Written by Georgia Wyatt

#9.16.2021 

#First part of the code is defining function: 


def doMath(x, y, c): #One function runs several math operations
    
   if c == 1: # c value determines function
    return(x + y)
   if c == 2:
    return x - y
   if c == 3:
    return x * y
   if c == 4:
    return round((x / y), 2)  #Round function, 2 is number of decimal places
   if c == 5:
    return x % y # Modulo symbol is % in python



# Take input from the user:

a = int(input("Enter first number: ")) 
b = int(input("Enter second number: "))

# This part of the code plugs input variables into doMath function: 
print("Sum:\t\t" + str(doMath(a, b, 1))) #str necessary to prevent concatenate error
print("Difference:\t" + str(doMath(a, b, 2)))
print("Product:\t" + str(doMath(a, b, 3)))
print("Quotient:\t" + str(doMath(a, b, 4)))
print("Modulo:\t\t" + str(doMath(a, b, 5)))
   


