
import random  
import string
import time

#welcoming the user
name = input("What is your name?")
print("Hello," +name, "time to play hangman!")

time.sleep(2)

print ("Are you ready...Let's go")

WORDLIST_FILENAME = "words.txt"


def load_words():
	"""
	Returns a list of valid words. Words are strings 
	of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	time.sleep(2)
	print("Loading word list from file...")
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	# line: string
	line = inFile.readline()  # Read until EOF using readline()
	# wordlist: list of strings
	wordlist = line.split() #  splits or breakup a string  using a defined separator.
	time.sleep(1)
	print("  ", len(wordlist), "words loaded.") #len returns the length of a specific string
	return wordlist






def choose_word(wordlist):
	"""
	wordlist (list): list of words (strings)
	
	Returns a word from wordlist at random
	"""
	return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()






def is_word_guessed(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing;
	 assumes all letters are
	  lowercase
	letters_guessed: list (of letters), which letters 
	have been guessed so far;
	  assumes that all letters are lowercase
	returns: boolean, True if all the letters of 
	secret_word are in letters_guessed;
	  False otherwise
	'''
	
	for i in secret_word:
		if i in letters_guessed:
			return True
		else:
			return False

	


def get_guessed_word(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing
	letters_guessed: list (of letters), which letters 
	have been guessed so far
	returns: string, comprised of letters, underscores (_), 
	and spaces that represents
	  which letters in secret_word have been guessed so far.
	'''
	string = " "
	for i in secret_word:
		if i in letters_guessed:
			string+=i
		else:
			string+="_ "
	return string			

def get_available_letters(letters_guessed):

	'''
	letters_guessed: list (of letters), which letters have
	 been guessed so far
	returns: string (of letters), comprised of letters that 
	represents which letters have not
	  yet been guessed.
	  '''
	#fill not guessed with alphabet a-z
	not_guessed=[]
	for i in range(26):
		not_guessed+=chr(i+ord("a"))
	for j in letters_guessed:
		not_guessed.remove(j)
	string=""
	for k in not_guessed:
		string +=k
	return string				


	

def hangman(secret_word):

	'''
	secret_word: string, the secret word to guess.
	
	Starts up an interactive game of Hangman.
	
	* At the start of the game, let the user know how many 
	  letters the secret_word contains and how many guesses
	   s/he starts with.
	  
	* The user should start with 6 guesses

	* Before each round, you should display to the user how 
	many guesses
	  s/he has left and the letters that the user has not yet 
	  guessed.
	
	* Ask the user to supply one guess per round. Remember to 
	make
	  sure that the user puts in a letter!
	
	* The user should receive feedback immediately after each 
	guess 
	  about whether their guess appears in the computer's word.

	* After each guess, you should display to the user the 
	  partially guessed word so far.
	
	Follows the other limitations detailed in the problem
	 write-up.
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	time.sleep(1)
	print ("welcome to the game hangman!\n")
	time.sleep(1)
	print ("I am thinking of a word game that is "+str(len(secret_word)) +" letters long")
	print ("*****************")
	letters_guessed = []
	guesses=10
	#while all the letters of secretword are not yet in lettersGuessed and guesses left is more than 0
	while not is_word_guessed(secret_word,letters_guessed) and guesses >0:
		#print first line
		print("you have "+str(guesses)+" guesses left")
		#print second line
		print ("Available letters: "+get_available_letters(letters_guessed))
		#print third line
		#if user input a letter that has already been entered,reprompt for letter
		while True:
			guessLetter= input("please guess a letter:").lower()
			if guessLetter in letters_guessed:
				print ("Oops! you have already guessed that letter:"+get_guessed_word(secret_word,letters_guessed))
				print ("*****************")
				print("you have "+str(guesses)+" guesses left")
				print("Available letters:"+get_available_letters(letters_guessed))
			else:
				break
		letters_guessed+=guessLetter	
		#print last line
		#if correctly guessed secret word
		if  is_word_guessed(secret_word,letters_guessed):
			print ("Good guess:"+get_guessed_word(secret_word,letters_guessed))
			print ("*****************")
			print("congratulations ,You won!")
			break
		#else if the guess letter is in secret word	
		elif guessLetter in secret_word:
			print("Good guess:"+ get_guessed_word(secret_word,letters_guessed))
			print ("*****************")
		#else the guess letter is not in secret word
		else:
			print("Oops! that letter is not in my word:"+get_guessed_word(secret_word,letters_guessed))
			print ("*****************")
			guesses-=1
		#if ran out of guesses
		if guesses==0:
			print("Sorry,you ran out of guesses.The word was "+secret_word+".")



									




if __name__ == "__main__":
	# pass

	# To test part 2, comment out the pass line above and
	# uncomment the following two lines.
	
	secret_word = choose_word(wordlist)
	hangman(secret_word)
