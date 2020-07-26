# 6.00 Problem Set 3
# 
# Hangman
#
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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
    wordlist = str.split(line)
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

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def partial_word(word, guessed_letter):
    result = ''
    for letter in word:
        if letter in guessed_letter:
            result = result + letter
        else:
            result = result + ' '

    return result

def hangman():
    random_word = choose_word(wordlist)
    word = random_word.lower()
    print('I am thinking of a word that is', len(word), 'letters long.')
    chance = 8
    guessed_letter = ''
    word_guessed = False
    available = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                         'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while chance > 0 and not word_guessed :
        print('________________')
        print('You have', chance, 'chances.')
        print('Available letters : ', ''.join(available))
        guess = input('Enter your guessing letter : ')
        if guess not in available:
            print('Oops! You\'ve already guessed that letter : ', partial_word(word, guessed_letter))
        elif guess not in word:
            chance = chance - 1
            print('Oops! That letter is not in my word : ', partial_word(word, guessed_letter))
            available.remove(guess)
        else:
            available.remove(guess)
            guessed_letter = guessed_letter + guess
            print('Good guess : ', partial_word(word, guessed_letter))

        if word == guessed_letter:
            word_guessed = True

    if word_guessed:
        print('Congratulation!')
    else:
        print('You are hanged!!')









