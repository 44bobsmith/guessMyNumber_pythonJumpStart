import random

user = input('What is your name please?')

the_number = random.randint(0, 100)
guess = -1

while guess != the_number:
    guess_text = input('Please guess a number from 0 to 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('{} your guess {} was too LOW'.format(user, guess))
    if guess > the_number:
        print('{} your guess {} was too HIGH'.format(user, guess))
    if guess == the_number:
        print('Nice job {}! The number is {}'.format(user, guess))
