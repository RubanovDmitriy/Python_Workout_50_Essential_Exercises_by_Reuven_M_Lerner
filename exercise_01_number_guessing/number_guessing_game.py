import random


def guessing_game():
    number = random.randint(0, 100)

    while True:
        guess = int(input('Guess number: '))

        if number > guess:
            print(f'Your guess of {guess} is too low!')

        elif number < guess:
            print(f'Your guess of {guess} is too high!')

        elif number == guess:
            print(f'Right! The answer is {guess}')
            break


guessing_game()
