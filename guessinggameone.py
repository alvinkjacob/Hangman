import random

random_number = int(random.randrange(1, 10))
guess = 0


while guess != str(random_number):
    guess = input("Guess a number between 1 and 9: ")

    if guess.lower() == "exit":
        break
    if guess < str(random_number):
        print("This is too low.")
    elif guess > str(random_number):
        print("This is too high.")
    else:
        print("You have guessed correctly!")
