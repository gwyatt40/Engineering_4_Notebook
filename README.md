# Engineering_4_Notebook
## Hello Raspberry Pi: 
#### Filename: hello_world.py
#### Directories: pi@raspberrypi:~/Documents/Python$
#### Description: 
Prints text “Hello World!” 10 times, each on a new line. 

### Result: 


### Code: 

<details>
  <summary> Hello, World Code </summary>
        
``` 
   for i in range (10): 
        print ("Hello, World")
        
```


</details>


### Terminal Commands: 
- cd DirName - opens directory (directory names are case sensitive!) 
- mkdir FolderName - creates directory
- cd .. - go back a directory (remember space!) 
- cd - - go back a directory (remember space!) 
- pi@raspberrypi:~/Directory1/Directory2$ - you are working within these folders 
- Type command python from terminal to start python interpreter. Should see: Type "help", "copyright", "credits" or "license" for more information.
>>>
- exit () - exit python interpreter 
- nano filename.py to open a python file (must be in terminal) 
- python filename.py - runs this python file 
- clear - clears terminal screen (but saves info, directories etc) 
- SHUTDOWN: sudo shutdown -h now
- sudo nano /etc/profile add export TERM=xterm to bottom of file save, exit, and reboot py for color change
### Python Commands: 
- print (“Hello World!”) - prints text in quotations 
- ctrl x, y, enter - save and exit python file editor 
- for i in range (val): - runs indented command on next line val number of times 
- k^ = cut text
- u^ = paste uncut text
- Additional Info: 
- Pin plug in order: outside row near SD card. Red, space, black, white, green. 


## Github Set Up:  
### Assignment: 
Connection to github push readme and python files. 

### Git Commands: 
- git add filename - adds file to git
- git config --global user.email "gwyatt40@charlottesvilleschools.org" - ID 1
- git config --global user.name "gwyatt40" - ID 2
- git commit - commits files
- git commit -m “message” - commits files with message
- git push origin main - push changes to git 
- Username - gwyatt40
- PAT Access (password): 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 (copy with no spaces!!!!!)  
- Copy (from outside): ctrl+C Paste(into BeagleTerm): ctrl+shift+V

## Hello Python
#### Filename: dice_roller.py
#### Description:
Create a dice roller code in python.
### Result:
<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/dice_roller_screenshot.png" alt="Dice Roller Results" width="400" height="300">


### Code:
<details>
  <summary>Automatic Dice Roller Code</summary>

 ```
# Automatic Dice Roller

# Written by Georgia Wyatt

# 9.15.21
        
# Import libraries for random number gen 
import random
from random import randint 
     
# Print initial instructions
print ("Automatic Dice Roller")
print ("Press enter to roll")

#Roll dice function 
def roll_dice(): 
    roll = random.randint(1,6)
    print("You rolled a %d " % roll)
    print("Press enter twice to roll again")
    print ("Press x + enter to quit")

# Continuous while True loop runs function with enter, exits with x      
while True: 
    enter = input("")
    if enter == '':  # hitting enter == ''  empty string
        roll_dice()
    x = input("")
    if x:
        print("Goodbye!")  
        break 

```
</details>

### Python Commands: 
- import random from random import randint - Import random numbergen libraries
- while True- Endless loop function
- n = input("") - Sets a key as input when pressed
- if - If statement, if this is true then do this
- def function(): - Define actions involved in a function
- roll = random.rantint(x,y) - Randomly generate a number between x and y
- %d % roll- Prints generated number
- break - Ends loop and exits program

### Reflection: 
- Ran into indent issues often. Deleting extraneous functions left over from copying code fixed this. 
- Tried using an exit() function and failed. break is the command to end the loop and exit.
- while True loop keeps program from ending as soon as number is generated. 
### Helpful links: 
- I based my code around [this discussion](https://stackoverflow.com/questions/47560026/how-to-get-python-3-to-use-enter-as-an-input/47560057) from Stack Overflow. 


## Python Program 01 Calculator (Hello Functions
#### Filename: python_calculator1.py
#### Description: 
 Create a calculator that, when given two numbers, can carry out five operations (add, subtract, multiply, divide, modulo)
