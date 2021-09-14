

import random

def roll_dice():
    roll = random.randint(1,6)
    print("You rolled a %d " % roll)
    print("Press enter twice to roll again")
    print ("Press x + enter to quit")


def main():
    
    
    print("") #if I remove this print function I get an indent error

while True: 
    print ("Automatic Dice Roller")
    print("Press enter to roll")
    enter = input("")
    if enter == '':  # hitting enter == ''  empty string
        roll_dice()
    x = input("")
    if x:
        print("Goodbye!")  
        break
        
 

    
    
main()