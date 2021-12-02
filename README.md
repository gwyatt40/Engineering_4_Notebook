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
- python3 filename.py - runs this python file 
- clear - clears terminal screen (but saves info, directories etc) 
- SHUTDOWN: sudo shutdown -h now
- sudo nano /etc/profile add export TERM=xterm to bottom of file save, exit, and reboot py for color change
- ctrl+C to exit running a file
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
- PAT Access: found in PAT code document, cannot commit this code into git readme
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
Create a code that runs a game of hangman. One person inputs a word, and then another player guesses letters. If the player guesses all the letters correctly, they win. If they guess a letter wrong, the screen draws part of the hangman, and if the full hangman is drawn, the player loses.
  ### Results
  <img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Hangman1.png" alt="Strings and Loops Results" width="325" height="">
  <img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Hangman%202.png" alt="Strings and Loops Results" width="325" height="">
	
### Code
  <details>
  <summary> Hangman Code </summary>
	  
```        
import sys #system specific parameters/functions
def hangman():
	print("Hangman time!")
	word=input("Player 1, input your word: ")

	print('\n'*20) 
	# original code used getpass() to make input invisible as a password
	# in this code, player 1 can still see their input, but it disappears with 'enter'for player 2 

	start_game(word)

def start_game(word):
	player_lives = 7 #player lives correspond with visuals 
	used_letters =[]
	number_dashes=["_" for i in range(len(word))] #one _ per letter in word

	# prints visuals and dashes based on word/lives
	print(visuals(player_lives))
	print("")
	print("")
	print(" ".join(number_dashes))

	while player_lives == player_lives:

		input_letter =input("Player 2, input your letter guess: ") # takes input from player 2
		print('\n'*20)
		if len(input_letter) > 1: #rejects input if more than one letter 

			player_lives-= 1 #removes a life
			print(visuals(player_lives)) #prints new visuals
			print(input_letter,"is not \'a letter\'!") 
			print("Used letters:"," ".join(used_letters)) # prints used letters
			print((updated_dashes(word,input_letter,number_dashes,)),'') #prints dashes


		elif input_letter  not in used_letters and input_letter in word: # correct guess

			print(visuals(player_lives)) #lives unchanged
			print("Correct,",input_letter,"is in the word!")
			if input_letter not in used_letters: 
				used_letters.append(str(input_letter)) #adds to used letters
			else:
				pass
			print("Used letters:"," ".join(used_letters)) # this is necessary to print used letters/dashes, not repetitive! 
			print((updated_dashes(word,input_letter,number_dashes,)),'')
			
		elif input_letter not in word: #incorrect guess
			player_lives-=1 #removes life 
			print(visuals(player_lives)) # prints new visuals 
			print("Incorrect,",input_letter,"is not in the word")
			if input_letter not in used_letters:
				used_letters.append(str(input_letter)) #adds to used letters
			else:
				pass
			print("Used letters:"," ".join(used_letters)) #prints used letters and dashes
			print((updated_dashes(word,input_letter,number_dashes,)),'')

		elif input_letter in used_letters: #already guessed letter

			player_lives-=1 #removes life
			print(visuals(player_lives)) #prints new visuals 
			print("You already guessed",input_letter)
			if input_letter not in used_letters:
				used_letters.append(str(input_letter)) #adds to used letters (seems repetitive but is necessary for printing) 
			else:
				pass
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')

		if player_lives == 0: #no more lives/dead! 
			you_lose(player_lives,word) #runs loss function

		elif word == "".join(number_dashes): #word guessed correctly
			you_win(player_lives,word) #runs win function 

def updated_dashes(word,input_letter,number_dashes): #function for printing dashes and guessed letters

	for i in range(len(word)):

		if input_letter == word[i]:

			number_dashes[i] = input_letter

	return (" ".join(number_dashes))

def you_lose(player_lives,word): # loss function

	print("The guesser loses!","The word was",word)
	sys.exit()

def you_win(player_lives,word): #win function


	print("""
 °˖✧   ☆  ★ °˖✧   ･✧★  *:･ﾟ✧✧     ✧ ･ﾟ✧✧ 
 ☆★  °˖     ✧    :･ﾟ ✧ ･ﾟ✧✧ ･ﾟ★✧✧ ･  ✧ ★*: ･ﾟ
  ✧ * ･ﾟ✧✧ : """)



	print("The guesser wins!!", "The word was", word)
    


	print("""
 °˖✧   ☆  ★ °★˖✧   ･★✧  *:･ﾟ✧✧ : ･ﾟ
 ☆★      °˖✧    :･ﾟ✧★ ★°˖✧°˖✧° ✧°˖✧*: ･ﾟ
    ✧  *: """)
    

	sys.exit()

def visuals(player_lives): #prints visuals coressponding with player lives, added an extra so now 7

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

### Python Commands

### Reflection
  I found this code online and minorly changed it to make it fit my project. I removed the getpass() function from the player one input, altered the visuals, and added an additional player life so that the hangman drawing made more sense (one arm at a time instead of both). I attempted to delete certain portions of the code that I thought seemed repetitive, but found that they were necessary for consistently printing the dashes and used letters (see code comments). If I were to spend more time on this project I would add in an option to guess the word after every correct letter guess, which I attempted initially but found that it would require substantial reworking of the rest of the code. 
### Helpful Links 
I sourced the entire code from [this Github Gist](https://gist.github.com/Petersonp/9aac42c7b3e577e952ac1f7b3523e370)
	

 ## Skateboard (CAD Intro 2.1-2.4)
	
 
 #### File: [Skateboard](https://cvilleschools.onshape.com/documents/1da03e0163ff9ca5442c99a6/w/6468065e9e72fb573e9fa934/e/dcb6e77e42efeebf0c3d7371?renderMode=0&uiState=6176b2331d0d684e60e85501)
 
 ### Description 
   Building the deck, wheel, and trucks of a skateboard in Onshape following [this tutorial](https://cvilleschools.onshape.com/documents/ce5ac8909ec93f2ab937afda/w/77af2f4715cd6b9dc0f3d968/e/1cf175a4a9e7faeb7db52e25)
 
 ### Results
#### Full Assembly
<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Skateboard%20CAD%20Full%20Assembly.png" alt="Skateboard Assembly Results" width="375" height="">

#### Deck
 <img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Skateboard%20CAD%20Deck%20.png" alt="Skateboard Deck Results" width="375" height="">

#### Trucks 
  <img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Skateboard%20CAD%20Trucks%20.png" alt="Skateboard Trucks Results" width="250" height="">

#### Wheel and Bearing 

<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Skateboard%20CAD%20Wheel%20and%20Bearing.png" alt="Skateboard Wheel and Bearings Results" width="350" height="">
	
### Onshape Tips
  - Always name parts! Also name individual features (sketches/extrudes/etc). 
  - Can extrude a sketch without having to close the sketch and reselect it 
  - Pressing the 'N' key rotates to normal view
  - Offset tool to start new geometry a specific distance and angle away from a sketch
  - You can select to insert an entire part studio into an assembly
  - 'Flip primary axis' to rotate fasten mates
  - Make sure to select the correct mate connectors

 
### Reflection
- I didn't specifically name features for this assignment because the tutorial used default element names (ex. "Sketch 2"), but for future assignments without a tutorial I definitely will. 
- I initially tried to use Onshape on my Chromebook but found that it is much easier on a desktop with a mouse
- Using view shortcuts ('N' key for normal) and selecting faces to rotate to saves time 
- This assignment was mostly an overview of skills I'd used in the past with Onshape. It was most helpful to be reminded of how to use Onshape's assemblies, which I had had limited practice with. Mate connectors especially were important to review.
	
## Bricks and Configurations (CAD Intro 3.1-3.4)

#### File: [Bricks](https://cvilleschools.onshape.com/documents/f94d2454fca8e82433d22c88/w/f71befabc11c5a68117b7ec1/e/c65758b4e27f55fd2208b800?configuration=List_3hIsBFnRiF81ll%3D_1x4%3BList_5jXFJwDC3SGwnX%3DPlate%3BList_sOrjlIFxJ9oFKv%3DDefault&renderMode=0&rightPanel=configPanel&uiState=6183e98ca6a3d440b44865b5)
 
### Description
Build a 2x4 Lego brick (3.1), create configurations for its size and color (3.2), use configured bricks to build a Lego duck (3.3), and create a set of instructions in OnShape drawings for building with bricks (3.4). 
	
### Results

#### Examples of Brick Configurations
<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Brick%20Configuration%201.png" alt="Brick Configuration 1" width="250" height="125"><img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Brick%20Configuration%202.png" alt="Brick Configuration 2" width="250" height="125">
	
	
<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Brick%20Configuration%203.png" alt="Brick Configuration 3" width="250" height="125"><img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Brick%20Configuration%204.png" alt="Brick Configuration 3" width="250" height="125">


#### Brick Duck 
<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Brick%20Duck.png" alt="Brick Configuration 3" width="450" height="325">

#### Brick Duck Drawings
	
<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Brick%20Duck%20Drawing%201.png" alt="Brick Duck Drawing 1" width="450" height="325"> <img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/Brick%20Duck%20Drawing%202.png" alt="Brick Duck Drawing 2" width="450" height="325">


### OnShape Tips
- Typing '#' while in dimension allows you to create a new variable immediately or to call an old one (3.1)
- Pay attention to automatic constraints (yellow lines when sketching), avoid these if unwanted (3.1)
- Variables can be added/subtracted/multiplied/divided by or with other values in dimensions (ex. 1.8mm-#height) (3.1)
- Clicking and dragging the left side of the configuration panel allows you to change its size (3.2)
- Likewise, dragging the bottom of the configurations tap at the top left side of the screen allows you to change its size (3.2)
- To select features of a part to configure, select "configure features" and then select the feature so that it is outlined in yellow (3.2)
- Checking or unchecking the 'Unsuppressed' box for a feature allows you to supress/unsuppress that feature and can be selected as a configuration feature (3.2)
- Certain features such as [Part Color](https://cvilleschools.onshape.com/documents/d997b0ffc30f659113b10c00/v/347f7240ed6eefd77e80907e/e/a59f52547080e509330b02f7) and [Part Name](https://cvilleschools.onshape.com/documents/f4d470584fdeef9603415532/v/0c632933b6aca3d2608fda5d/e/acddbbed81af3772a07adf21) must be added in from their seperate pages (3.2) 
- Snap mates involve left-clicking and dragging mate connectors together. Q key to rotate. Check box to fasten. (3.3)
- Selecting 'mass relative to mate connector' and choosing a mate connector in the mass properties tab allows you to find the center of mass relative to that mate connector (3.3) 
- Right-click selecting an assembly in the tool bar will allow you to create a drawing of that assembly (3.4)
- Right-selecting a view in the drawing and selecting 'show/hide' will allow you to add/remove shading (3.4)
- The bill of materials (BOM) is located and can be edited in the right tab of an assembly above the configurations tab (3.4)
- The orange reload button at the top left of the drawing page refreshes the drawing and updates it with changes from edits to parts and assemblies (3.4)
- Checking/unchecking the 'explode lines' box in an explode feature ('Explode 1') allows you to add/remove explode lines (3.4)
- To create callouts you must select the edge or vertex of a part, not the face (3.4)


### Reflection 
- 3.1: I learned how to create and assign variables for part dimensions. I also learned how to create mate connectors and assign them coordinates. The most difficult part of this was making sure that variable values were in the correct order, for example "8*#cols" instead of "8#*cols. 
- 3.2: I learned how to create configurations by selecting certain features in the configurations tab, which was really mostly review. The part of this section that was new to me was having to add in certain configuration types (part name and part color) from seperate pages. 
- 3.3: I learned how to use snap mates in an assembly which makes assemblies much easier by allowing you to drag together mate connectors. I also learned how to drag to select assembly parts in order to select center of mass and also how to set center of mass relative to a mate connector. The most difficult part of this section was ensuring that the correct mate connectors were snapped together. 
- 3.4: I learned how to create drawings of assemblies in OnShape, a feature which I did not know existed before this assignment. The most difficult part of this section was organizing features within the drawings to make them presentable, and ensuring that the features themselves were composed correctly (exploded view was mostly equidistant, etc.). 


## GPIO LED Blink 
#### File: [led1.py](https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Python/led1.py)
	
### Description 
Use GPIO pins on a Raspberry Pi to alternate blinking two LEDS, print which LEDs are on an which are off, blinking should continue until ctrl+c exits program. 
	
### Results

#### Print Screen
<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/LEDBlinkPrint.png" alt="LED Print" height="300">

#### LED 1 On
<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/LED%20Blink%201.png" alt="LED 1 On" width="400" >

#### LED 2 On
<img src="https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Images/LED%20Blink%202.png" alt="LED 2 On" width="400" height="350">
	
### Code 
	
<details>
  <summary> LED Blink Code </summary>
        
``` 

# Python Program - LED BLINK
# Georgia Wyatt
# 11/30/21

# import LED and time libraries
from gpiozero import LED
from time import sleep

# assign pins
led1 = LED(21)
led2 = LED(13)

while True: # loops constantly until ctrl+C
    led1.on() # red on
    led2.off() # green off 
    print("RED ON, green off") # prints to screen
    sleep(1) # 1 second pause
    led1.off() # red off 
    led2.on() # green on 
    print("red off, GREEN ON") # prints to screen
    sleep(1) # 1 second pause
	
	
```
</details>

#### Wiring
- Connecting the positive side of LED 1 to pin 21 and the negative to a resistor to ground. 
- Connecting the positive side of LED 2 to pin 13 and the negative to a resistor to ground. 
- Pictured in results images above. 

### Reflection
- Must indent using either all spaces or all tabs, using both results in an error
- LED Wiring: PIN- Positive-LED-Negative-Ground
- Remember to git pull before pushing 
- Don't alter wiring at all while Pi is still on and plugged into computer! 
- while True loops will only cancel with ctrl+c unless exit function is added to the code
- Instead of printing to a separate serial monitor like with arduino, running print functions in Python prints to the main screen
- Must import sleep "from time input sleep" in order to use sleep functions
- Must import GPIO LED "from gpiozero import LED" to use led.on() and led.off() functions with GPIO pins

### Helpful Links
- I based my code around [this LED blink code](https://www.tunnelsup.com/raspberry-pi-zero-blink-an-led-using-gpio-pins/) from tunnelsup.com

## RPi Safe Shutdown Button 
	
#### File: [shutdown.py](https://github.com/gwyatt40/Engineering_4_Notebook/blob/main/Python/shutdown.py)
	
### Code 
<details>
  <summary> Safe Shutdown Code </summary>
        
``` 


# safe_restart_shutdown_interrupt_Pi.py
#
# Raspberry Pi Safe Restart and Shutdown Python Script
# WRITTEN BY: Matthew Miller @ CHS
# MODIFIED: 11/30/2021
# DESCRIPTION: This python script uses a button to safely
# reboot/shutdown your RPi. A momentary press reboots the pi,
# holding the button shuts the RPi down. 
#
# Based on code from the following tutorial:
#https://learn.sparkfun.com/tutorials/raspberry-pi-safe-reboot-and-shutdown-button/
all
#-------------------------------------------------
import time
import RPi.GPIO as GPIO 
# Pin definition
reset_shutdown_pin = 26
# Suppress warnings
GPIO.setwarnings(False)
# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)
# Use built-in internal pullup resistor so the pin is not floating
GPIO.setup(reset_shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# modular function to restart Pi
def restart():
    print("restarting Pi")
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
# modular function to shutdown Pi
def shut_down():
    print("shutting down")
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
while True:
    #short delay, otherwise this code will take up a lot of the Pi's processing 
power
    time.sleep(0.5)
    # wait for a button press with switch debounce on the falling edge so that this
script
    # is not taking up too many resources in order to shutdown/reboot the Pi safely
    channel = GPIO.wait_for_edge(reset_shutdown_pin, GPIO.FALLING, bouncetime=200)
    if channel is None:
        print('Timeout occurred')
    else:
        print('Edge detected on channel', channel)
        # For troubleshooting, uncomment this line to output button status on 
command line
        #print('GPIO state is = ', GPIO.input(reset_shutdown_pin))
        counter = 0
        while GPIO.input(reset_shutdown_pin) == False:
            # For troubleshooting, uncomment this line to view the counter. If it 
reaches a value above 4, we will restart.
            #print(counter)
            counter += 1
            time.sleep(0.5)
            # long button press
            if counter > 4:
                shut_down()
        #if short button press, restart!
        restart()
	
```
</details>	
