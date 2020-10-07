the_word = input("What is the secret word? ")
print("\n" * 10)
blank = ("_" * len(the_word))
print(blank)
blank = list(blank)
lives = 10

while blank != list(the_word):
    guess = input("Guess a letter: ")
    print(" ")
    if guess.lower() in the_word:
        print("Correct.")
        print(" ")
        index = the_word.find(guess)
        blank[index] = guess
        print(''.join(blank))
    if guess not in the_word:
        print("Wrong.")
        print(" ")
        lives -= 1
        print(f"You have {lives} lives left.")
        if lives == 0:
            print("You have run out of lives.")
            print(" ")
            print(f"The word was {the_word}.")
            exit()
print(" ")
print("Well Done! You have guessed the word correctly.")
print(f"You had {lives} lives left.")
