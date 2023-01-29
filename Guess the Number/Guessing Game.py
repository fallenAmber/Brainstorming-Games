import random

def user_guess (number):

    rand_number = random.randint(1,number)

    guess = 0

    while guess!=rand_number:

        guess = int(input(f"Guess a number between 1 and {number}: "))

        if guess> rand_number:
            print(f"No, the number is too high.")
        elif guess<rand_number:
            print(f"No, the number is too low.")

        else:
            print(f"Yes, the correct guess is {guess}.")

#user_guess(10)

def computer_guess(number):

    low = 1
    high = number

    feedback = ''

    while feedback !='c':

        if low!=high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high(H), too low(L) or too correct(C)? ").lower()

        if feedback=='h':
            high = guess-1
        elif feedback =='l':
            low = guess+1


    print(f"Boo Hoo! The computer guessed your number {guess} correctly.")



computer_guess(100)