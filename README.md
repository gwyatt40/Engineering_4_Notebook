# Engineering_4_Notebook
## Hello Raspberry Pi: 
### Filename: hello_world.py
### Directories: pi@raspberrypi:~/Documents/Python$
### Description: Prints text “Hello World!” 10 times, each on a new line. 


### Code: 

``` 
for i in range (10): 
        print ("Hello, World")
        
```

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
### Assignment: connection to github push readme and python files. 

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
### Description: create a dice roller code in python 
### Filename: dice_roller.py



 ```
# Automatic Dice Roller

# Written by Georgia Wyatt

# 9.15.21

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


```
</details>
