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
	  
