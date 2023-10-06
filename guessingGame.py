import random

number = random.randint(0,9)
chances = 5
while chances > 0 :
    guess = int(input('Guess the number: '))
    if guess == number :
        print('You Won!')
        break
    elif guess < number :
        print('Your number is too low. Guess a number higher than ', guess)
        guess=guess-1
    elif guess > number :
        print('Your number is too high. Guess a number lower than ', guess)
        guess-guess-1
if chances == 0 :
    print('You Lose! The number is ', number)
