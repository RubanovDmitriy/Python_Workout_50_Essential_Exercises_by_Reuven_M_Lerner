import random

'''
Try the same thing, but have the program choose a random word from the dic-
tionary, and then ask the user to guess the word. (You might want to limit your-
self to words containing two to five letters, to avoid making it too horribly
difficult.) Instead of telling the user that they should guess a smaller or larger
number, have them choose an earlier or later word in the dict.
'''

WORK_DICT = {
    1: 'cat',
    2: 'dog',
    3: 'news',
    4: 'head',
    5: 'arm',
    6: 'rot',
}


def guessing_game():
    number = random.randint(1, 6)

    print(WORK_DICT)

    while True:
        guess = input('Guess word: ')

        if number > list(WORK_DICT.keys())[list(WORK_DICT.values()).index(guess)]:
            print(f'Your guess of {guess} is too low!')

        elif number < list(WORK_DICT.keys())[list(WORK_DICT.values()).index(guess)]:
            print(f'Your guess of {guess} is too high!')

        elif number == list(WORK_DICT.keys())[list(WORK_DICT.values()).index(guess)]:
            print(f'Right! The answer is {guess}')
            break


guessing_game()
