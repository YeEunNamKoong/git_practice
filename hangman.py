import random

words = ['infection','internet','distance','corona','mask','zoom']

correct_guesses = set()

word = random.choice(words)
letters = set(i for i in word)
lives = 10

def collect_guesses(correct_guesses,current_guess):
    correct_guesses.add(current_guess)
    return correct_guesses

def make_mask(correct_guesses,word):
    mask = ''
    for i in word:
        if i in correct_guesses:
            mask += f'{i}.'
        else:
            mask += '_.'
    return mask


while lives > 0:
    current_guess = input("Please input your letter: ")
    if current_guess in letters:
        correct_guesses = collect_guesses(correct_guesses,current_guess)
        mask = make_mask(correct_guesses,word)
        print(mask)
    else: 
        lives -=1
        print(f"You lost your life, you have {lives} lives, try it again")
        if lives == 0:
                print(f"You lost all your lives, the word was {word}.")

    if len(letters) == len(set(correct_guesses)):
        break

print ("You won, nice job")
