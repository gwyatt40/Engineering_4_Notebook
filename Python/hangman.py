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
			
		elif input_letter not in word:
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

def you_lose(player_lives,word):

	print("The guesser loses!","The word was",word)
	sys.exit()

def you_win(player_lives,word):


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
	  
