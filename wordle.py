from random import randint
#import pygame as pg
#import sys

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

credible = ''
with open('wordle_credible.txt', 'r') as temp:
    credible = temp.readlines()[0]
    credible = credible.replace('\"', '')
    credible = credible.replace(',', ' ')
    credible = list(credible.split())


guessable = ''
with open('wordle_guessable.txt', 'r') as temp:
    guessable = temp.readlines()[0]
    guessable = guessable.replace('\"', '')
    guessable = guessable.replace(',', ' ')
    guessable = list(guessable.split())


def validate(word):
    #word needs to be five letters
    #word needs to be in guessable + credible
    if len(word) != 5:
        return 'input needs to 5 letters long'
    for i in range(0, 5):
        if not (97 <= ord(word[i]) <= 122):
            return 'input needs to be only letters'
    
    if word not in credible and word not in guessable:
        return 'invalid word'
    
    return True

index = randint(0, len(credible))
chosen = credible[index]

guess = ''
guesses = 0
recent = []
while (guess != chosen and guess != 'stop') and guesses < 6:
    guess = input().lower()
    msg = validate(guess)
    if msg == True:
        #check to see if letters are in and print colours
        #letter in right place
        #letter not in right place but in other parts of the word

        correct = []
        temp = list(chosen)
        for i in range(0, 5):
            if guess[i] == temp[i]:
                temp[i] = ''
                correct.append(i)
        misplaced = []
        for i in range(0, 5):
            if guess[i] in temp:
                temp[temp.index(guess[i])] = ''
                misplaced.append(i)
        
        output = ''

        for i in range(0, 5):
            if i in correct:
                output += bcolors.OK + guess[i] + bcolors.RESET
            elif i in misplaced:
                output += bcolors.WARNING + guess[i] + bcolors.RESET
            else:
                output += guess[i]

        recent.append(output)

        guesses += 1
    else:
        print(msg)

    for i in range(0, len(recent)):
        print(recent[i])
    print(f'\nguesses left = {6-guesses}\n')

if guesses <= 6 and guess == chosen:
    print(f'correct, you got it in {guesses} tries')
else:
    print('ran out of guesses')
    print(f'the word was {chosen}')