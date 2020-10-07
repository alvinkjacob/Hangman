def guess():
    print("Think of a number between 1 and 100: ")
    start = input("Are you ready to play? ")
    guess_number = 1
    number = 50

    if start.lower() == "yes":
        guess_one = input(f"Is your number {number}? ")
        while guess_one.lower() != "yes":
            if guess_one.lower() == "lower":
                guess_number += 1
                number = number - 1
                guess_one = input(f"Is your number {number}? ")
            elif guess_one.lower() == "higher":
                guess_number += 1
                number = number + 1
                guess_one = input(f"Is your number {number}? ")
            else:
                guess_one = input(f"Is your number {number}? ")
        if guess_one.lower() == "yes":
            print("Yay I won.")
            print(f"I took {guess_number} guesses to win.")
            exit()
    else:
        exit()


guess()
