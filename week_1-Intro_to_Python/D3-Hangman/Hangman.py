import random

# Now that we are familiar with using slice to modify the immutable, let's build Hangman.

def hangman():
    possible_phrases = ['cats are better', 'Hot CoffeE', 'vulpis', 'here ya go']
    phrase = possible_phrases[ random.randrange(len(possible_phrases)) ]
    displayed_phrase = set_board(phrase)
    tries = 10
    
    while phrase != displayed_phrase and tries > 0:
        prior_displayed_phrase = displayed_phrase
        print(f'{displayed_phrase} : You have {tries} guesses left.')
        
        guess = input('Guess a letter:  ')
        if len(guess) > 1: guess = input('Please guess just ONE letter!')
        for index in range(len(phrase)):
            if phrase[index].lower() == guess.lower():
                displayed_phrase = displayed_phrase[:index] + phrase[index] + displayed_phrase[index+1:]
        if prior_displayed_phrase == displayed_phrase: tries -= 1
    
    print(phrase, ': Was the correct answer.')
    if phrase == displayed_phrase: print('Yay, you won!')
    else: print('Try Again.')

def set_board(phrase):
    displayed_phrase = ''
    for letter in phrase:
        if letter == ' ': displayed_phrase += ' '
        else: displayed_phrase += "#"
    return displayed_phrase

while input('Would you like to play hangman? (Y/y').lower() == 'yes':
    hangman()