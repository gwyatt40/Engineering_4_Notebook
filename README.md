# Engineering_4_Notebook
## Hello Raspberry Pi 
#### Filename: hello_world.py
### Directories: pi@raspberrypi:~/Documents/Python$
### Description 
Prints text “Hello World!” 10 times, each on a new line. 

### Result 


### Code

<details>
  <summary> Hello, World Code </summary>
        
``` 
   for i in range (10): 
        print ("Hello, World")
        
```


</details>


### Terminal Commands 
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
### Python Commands 
- print (“Hello World!”) - prints text in quotations 
- ctrl x, y, enter - save and exit python file editor 
- for i in range (val): - runs indented command on next line val number of times 
- k^ = cut text
- u^ = paste uncut text
- Additional Info: 
- Pin plug in order: outside row near SD card. Red, space, black, white, green. 


## Github Set Up  
### Assignment
Connection to github push readme and python files. 

### Git Commands 
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
### Description
Create a dice roller code in python.
### Result
<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/dice_roller.png" alt="Dice Roller Results" width="400" height="300">


### Code
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

### Python Commands 
- import random from random import randint - Import random numbergen libraries
- while True- Endless loop function
- n = input("") - Sets a key as input when pressed
- if - If statement, if this is true then do this
- def function(): - Define actions involved in a function
- roll = random.rantint(x,y) - Randomly generate a number between x and y
- %d % roll- Prints generated number
- break - Ends loop and exits program

### Reflection
- Ran into indent issues often. Deleting extraneous functions left over from copying code fixed this. 
- Tried using an exit() function and failed. break is the command to end the loop and exit.
- while True loop keeps program from ending as soon as number is generated. 
### Helpful links 
- I based my code around [this discussion](https://stackoverflow.com/questions/47560026/how-to-get-python-3-to-use-enter-as-an-input/47560057) from Stack Overflow. 


## Python Program 01 Calculator (Hello Functions
#### Filename: python_calculator1.py
### Description 
Create a calculator that, when given two numbers, can carry out five operations (add, subtract, multiply, divide, modulo)

### Results

<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/python_calculator_1.png" alt="Python Calculator Results" width="450" height="325">

### Code
<details>
  <summary> Python Calculator 1 Code </summary>

```
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
   
```
</details>

### Python Commands
- % - Python symbol for modulo
- str - Defines as string, fixes int concatenate error
- round(n, z) - Rounds quantity (n) to the nearest z decimal places

### Reflection
- Can define variables directly in Python, don't need to state initially
- Modulo is the remainder between two numbers and in Python it is represented by % or 'mod'
- Int concatenate errors can be fixed by surrounding functions in str()
- Can put multiple if statements within one function, allowing it do take multiple actions depending on input
- I initially used five different functions before consolidating them into doMath(), doMath() could run each operation based on c variable input
- round() function rounds values either to whole numbers or to a specified number of decimal points (see Python Commands)

### Helpful Links
- I based my code around [this Github Gists example](https://gist.github.com/complxalgorithm/ee685852a2a37e88ebc8d64d2d126d91). I eliminated the function choice aspect and then consolidated the five functions into one, doMath(). 

## Quadratic Calculator
#### Filename: quadratic_calculator.py

### Description 
Calculates roots of a quadratic from input coefficients. 

### Results
<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/quadratic_calculator.png" alt="Quadratic Calculator Results" width="450" height="325">

### Code 

<details>
  <summary> Quadratic Calculator Code </summary>
        
``` 
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
        
```


</details>

### Python Commands
  - import cmath calls complex math library which contains sqrt and other functions
  - (-b+-cmath.sqrt(d))/(2*a) is the equation for the quadratic formila itself
  - d = (b**2) - (4*a*c) is the discriminant itself 
  
  
### Reflection
  - Most of this code involved using parts of other previous codes (ex. if x exit sequence)
  - The rest of it I found online (ex. discriminant and quadratic formula calculations)
  - The quadratic formula here could be set as a function initially instead of being written out later in the code
  - Spelling mistake in the results image was fixed later (the solutions are)
  
### Helpful Links
  - I based my code around [this example](https://www.programiz.com/python-programming/examples/quadratic-roots) from Programiz

 ## Strings and Loops
 
 #### Filename: stringsloops.py
 
 ### Description 
   Splits a phrase letter by letter on new lines. Types a - for spaces. 
 
 ### Results
  <img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/strings_and_loops.png" alt="Strings and Loops Results" width="325" height="">
  
 ### Code
  <details>
  <summary> Strings and Loops Code </summary>
        
``` 
print ("Enter phrase") # initial instructions

for x in input(): # takes input, input is string, so x is character in string
    if x == ' ': print('-') # replaces spaces with - signs
    else: print (x) # prints non space characters on new lines
        
```


</details>

### Python Commands
  - Since input is a string, taking x from input takes a single character 
  - if, else statement in this case means that characters print on seperate lines
 
### Reflection
  - Bob let me copy his code for this so shout out Bob!!!
  - I originally tried to do this using split() or list() functions but could not get the characters to print on separate lines and couldn't get the spaces to print as minus signs. I tried running a split() function to split into words, and then running list() functions on each word to split into letters, but this was much too complicated. 
  - Since strings are technically arrays, and the input here is a string, the code takes out individual characters from the array and defines them as x, it runs each character and prints it on a new line, unless it is a space, which it replaces with a - sign. 
  
 ### Helpful Links
  - Bob's code was from [this W3 Schools site](https://www.w3schools.com/python/python_for_loops.asp) originally. The site also has information on how to add loop breaks and other specifics to this program. 

## Hangman (MSP)
  #### Filename: hangman.py
  ### Description
  ### Results
  
  ### Code
  <details>
  <summary> Hangman Code </summary>
	  
```        
import sys
import getpass
def hangman():
	print("Hangman time!")
	word=input("Player 1, input your word: ")

	print('\n'*20)

	start_game(word)

def start_game(word):
	player_lives = 7
	used_letters =[]
	number_dashes=["_" for i in range(len(word))]

	print(visuals(player_lives))
	print("")
	print("")
	print(" ".join(number_dashes))

	while player_lives == player_lives:

		input_letter =input("Player 2, input your letter guess: ")
		print('\n'*20)
		if len(input_letter) > 1:

			player_lives-= 1
			print(visuals(player_lives))
			print(input_letter,"is not \'a letter\'!")
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')


		elif input_letter  not in used_letters and input_letter in word:

			print(visuals(player_lives))
			print("Correct,",input_letter,"is in the word!")
			if input_letter not in used_letters:
				used_letters.append(str(input_letter))
			else:
				pass
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')
			
			print("Press enter to guess word, press x to guess letter")
			enter = input("")
			if enter:
			    guess_word()
			x = input("")
			if x:
			    input_letter()
			
			


			player_lives-=1
			print(visuals(player_lives))
			print("Incorrect,",input_letter,"is not in the word")
			if input_letter not in used_letters:
				used_letters.append(str(input_letter))
			else:
				pass
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')

		elif input_letter in used_letters:

			player_lives-=1
			print(visuals(player_lives))
			print("You already guessed",input_letter)
			if input_letter not in used_letters:
				used_letters.append(str(input_letter))
			else:
				pass
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')

		if player_lives == 0:
			you_lose(player_lives,word)

		elif word == "".join(number_dashes):
			you_win(player_lives,word)

def updated_dashes(word,input_letter,number_dashes):

	for i in range(len(word)):

		if input_letter == word[i]:

			number_dashes[i] = input_letter

	return (" ".join(number_dashes))
	
def guess_word():
    guessword = input("Type your guess?")
    if guessword == word:
        you_win(player_lives,word)
    if guessword != word:
        print("Try again!")
        input_letter()
def you_lose(player_lives,word):

	print("The guesser loses!","The word was",word)
	sys.exit()

def you_win(player_lives,word):

	print("The guesser wins!","The word was",word)
	sys.exit()

def visuals(player_lives):

	if player_lives == 7:
		return"""
		_______
		|     |
		|     
		|
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 6:
		return"""
		_______
		|     |
		|     O
		|
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 5:
		return"""
		_______
		|     |
		|     O
		|     |
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 4:
		return"""
		_______
		|     |
		|     O
		|   --|
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 3:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|     
		|
		|
		|________
		|        |
		"""
	elif player_lives == 2:
	    return"""
		_______
		|     |
		|     O
		|   --|--
		|     |
		|    |
		|
		|________
		|        |
		"""
	elif player_lives == 1:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|     |
		|    | |
		|
		|________
		|        |
		"""
	elif player_lives == 0:
		return"""
		_______
		|     |
		|     O
		|    |||
		|     |
		|    | |
		|
		|________
		|! D E A D !|
		"""	
hangman()
 #runs hangman function
	  
```


</details>

### Reflection
  
### Helpful Links 
  I sourced the entire code from [this Github Gist](https://gist.github.com/Petersonp/9aac42c7b3e577e952ac1f7b3523e370)
