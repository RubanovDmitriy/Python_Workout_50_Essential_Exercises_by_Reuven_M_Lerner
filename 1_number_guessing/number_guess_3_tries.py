'Modify this program, such that it gives the user only three chances to guess the correct number.'
'If they try three times without success, the program tells them that they didn’t guess in time and then exits.'

import random


def guessing_game():
    number = random.randint(0, 100)
    max_guesses = 3
    guessed = False

    while max_guesses > 0:
        guess = int(input(f'You have {max_guesses} left, guess number: '))

        if number > guess:
            print(f'Your guess of {guess} is too low!')

        elif number < guess:
            print(f'Your guess of {guess} is too high!')

        elif number == guess:
            print(f'Right! The answer is {guess}')
            break

        else:
            print(f'You have exceeded the maximum of {max_guesses} guesses')

        if not guessed:
            max_guesses -= 1


guessing_game()
