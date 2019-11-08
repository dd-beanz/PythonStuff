# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    lettersArr = []
    guessArr = []
    guessArrFinal = []

    for letter in secret_word:
      lettersArr.append(letter)

    for letter in letters_guessed:
      if letter not in guessArr:
        guessArr.append(letter)

    for letter in secret_word:
      if letter in guessArr:
        guessArrFinal.append(letter)

    sortedLetters = sorted(lettersArr)
    sortedGuess = sorted(guessArrFinal)

    #print(''.join(sortedGuess))
    #print(''.join(sortedLetters))
    if sortedLetters == sortedGuess:
      return True
    else:
      return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    lettersArr = []
    guessArr = []
    guessArrFinal = []

    for letter in secret_word:
      lettersArr.append(letter)

    for letter in letters_guessed:
      if letter not in guessArr:
        guessArr.append(letter)

    for letter in secret_word:
      if letter in guessArr:
        guessArrFinal.append(letter)

    sortedLetters = sorted(lettersArr)
    sortedGuess = sorted(guessArrFinal)

    if sortedLetters == sortedGuess:
      return secret_word
    else:
      guessArrFinal = []
      for letter in secret_word:
        if letter not in guessArr:
          guessArrFinal.append('_ ')

        else:
          guessArrFinal.append(letter)

      return ''.join(guessArrFinal)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    allLetters = string.ascii_lowercase
    
    for letter in letters_guessed:
      if letter in allLetters:
        allLetters = allLetters.replace(letter,'')
    return allLetters
      

#def userInputProcessing(letterGuess,userLetterGuess,secret_word):


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    userLetterGuess = []
    vowels = ['a','e','i','o','u']
    userGuessCount = 6
    warningCount = 3
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',str(len(secret_word)),'letters long.')
    print('You have 3 warnings.')
    print(secret_word)
    print('---------------')
    
    while userGuessCount > 0:
      #Print amount of guesses left 
      print('You have', str(userGuessCount),'guesses left.')
      print('Available letters:', get_available_letters(userLetterGuess))
      #Append letter guess to list of guessed letters 
      letterGuess = input('Please guess a letter: ')
      if str.isalpha(letterGuess) == False:
        warningCount = warningCount - 1
        print('Oops! That is not a valid letter. You have', str(warningCount) ,'warnings left.')
        if warningCount == 0:
          print('You have lost a guess')
          userGuessCount = userGuessCount - 1
          warningCount = 3
      elif letterGuess in userLetterGuess:
        warningCount = warningCount - 1
        print('Oops! You have already picked that letter!. You have', str(warningCount) ,'warnings left.')
        if warningCount == 0:
          print('You have lost a guess')
          userGuessCount = userGuessCount - 1
          warningCount = 3
      else:
        userLetterGuess.append(letterGuess.lower())
        if letterGuess in secret_word:
          print('Good guess:', get_guessed_word(secret_word,userLetterGuess))
        else:
          print('Oops! That letter is not in my word:', get_guessed_word(secret_word,userLetterGuess))
          if letterGuess in vowels:
            userGuessCount = userGuessCount - 2
          else:
            userGuessCount = userGuessCount - 1
      if is_word_guessed(secret_word,userLetterGuess):
        break
      print('---------------')
      
    if userGuessCount > 0:
      print('Congratulations! You guessed the secret word!')
      total_score = userGuessCount * len(secret_word)
      print('Your score: ', str(total_score))
    else:
      print('Word was:',secret_word)
      print('You have ran out of guesses! Better luck next time!')
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    a = ''.join(my_word)
    word_without_space = ''.join(a.split())
    letter_count = 0

    if len(word_without_space) != len(other_word):
      return False
    
    else:
      for letter in my_word:
        if letter in other_word:
          letter_count = letter_count + 1
    if letter_count > 0:
      return True
    else:
      return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    letterCountMyWord = 0
    letterCount = 0
    words = []
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in my_word:
      if letter.isalpha():
        letterCountMyWord += 1
    for word in wordlist:
      if len(word) == len(my_word):
        letterCount = 0
        for letter in word:
          if letter in my_word:
            letterCount = letterCount + 1  
          else:
            letterCount = letterCount
        if letterCount == letterCountMyWord:
          words.append(word) 
    if len(words) == 0:
      print('No matches found.')
    else:
      print(words)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
