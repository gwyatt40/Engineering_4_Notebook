# Automatic Dice Roller

# Written by Georgia Wyatt

from random import randint

print ("Automatic Dice Roller")
print ("Press enter to roll")


import random

def roll_dice(): #Roll dice function 
    roll = random.randint(1,6)
    print("You rolled a %d " % roll)
    print("Press enter twice to roll again")
    print ("Press x + enter to quit")


def main():
    
    
    print("") #if I remove this print function I get an indent error for while True

while True: #continuous loop
    enter = input("")
    if enter == '':  # hitting enter == ''  empty string
        roll_dice()
    x = input("")
    if x:
        print("Goodbye!")  
        break #exits program
        
 

    
    
main()
