
#  The user first has to input their names and then, will be asked to guess any alphabet.
#  If the random word contains that alphabet, 
# it will be shown as the output(with correct placement) 
# and then the program will ask you to guess another alphabet or the word itself
#user can choose what they wanna guess.
#  The user will be given 12 turns(which can be changed accordingly) to guess the complete word.

import random
options = ['mango','fox','crow','pitch']
chosen = random.choice(options)
print(chosen)
input('what is ur name? ')

def proceed():
    guess = input('enter ur word guess\n')
    if guess == chosen:
        print(f'Congrats! You have guessed correctly in {g} turns')
        exit()
    
g=1
while g<=12:
    letter = input('guess ur letter: ')
    if letter in chosen:
        print(f'{letter} is in the {chosen.index(letter)+1}th position')
    else:
        print('try again')
    g+=1
    further = input('guess word?y/n:\n').lower()

    if further == 'y':
        proceed()
        print('wrong guess')
        g+=1
        print(f'you have guessed wrong {g} times')
        continue
    elif further == 'n':
        continue
    else:
        print('wrong input')
        quit()
