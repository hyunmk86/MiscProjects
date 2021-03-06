

import random
import string

WORDLIST_FILENAME = "(File path)"

def loadWords():


    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for l in secretWord:
        if l in lettersGuessed:
            return True
        else:
            return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    guessedword = ""
    for l in secretWord:
        if l in lettersGuessed:
            guessedword += l
        else:
            guessedword +=" _ "
    return guessedword

            

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    newlist = []
    usealpha = ""
    alpha = string.ascii_lowercase
    for char in alpha:
        newlist.append(char)
    for char in newlist:
        if char not in lettersGuessed:
            usealpha += char
    return usealpha

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guess = 8
    mistakes = 0
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    lettersGuessed = ''
    letterslist = []
    letterholder = ''
    while guess > 0:
        print "you have " + str(guess) + " left"
        print "available letters: " + getAvailableLetters(lettersGuessed)
        userinput = raw_input("Please guess a letter: ")
        lettersGuessed += userinput
        for char in lettersGuessed:
            letterslist.append(char)

        if userinput in letterholder:
            
            print "Oops ! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)

        if userinput not in secretWord and userinput not in letterholder:
                print "Oops ! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
                guess -= 1
                letterholder += userinput

        if userinput in secretWord and userinput not in letterholder:
                letterholder += userinput
                print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            print "Congratulation, you won!"
            break
        
    else:
        print "Sorry, you ran out of guesses. The word was " + secretWord
             
        
                



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
