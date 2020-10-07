player_one = input("Enter Player One name: ")
player_two = input("Enter Player Two name: ")

print(" ")

print(f"Hello {player_one} and {player_two}. Welcome to the game of 'Rock, Paper, Scissors!'")

print(" ")

proceed = input("Are you ready to play? ")

print(" ")

if proceed.lower() == "yes":
    print("Game Loading...")
else:
    exit()

print("Game has now loaded. ")

print(" ")


def game():
    first_move = input(f"{player_one}, make your move: ")
    second_move = input(f"{player_two}, make your move: ")

    print(" ")

    print(f"{player_one} chose {first_move}.")
    print(f"{player_two} chose {second_move}.")

    if first_move.lower() == "rock" and second_move.lower() == "paper":
        print(f"{player_two} has won.")
    elif first_move.lower() == "rock" and second_move.lower() == "scissors":
        print(f"{player_one} has won.")
    elif first_move.lower() == "rock" and second_move.lower() == "rock":
        print("Game has drawn.")
    elif first_move.lower() == "paper" and second_move.lower() == "paper":
        print("Game has drawn.")
    elif first_move.lower() == "paper" and second_move.lower() == "scissors":
        print(f"{player_two} has won.")
    elif first_move.lower() == "paper" and second_move.lower() == "rock":
        print(f"{player_one} has won.")
    elif first_move.lower() == "scissors" and second_move.lower() == "paper":
        print(f"{player_one} has won.")
    elif first_move.lower() == "scissors" and second_move.lower() == "scissors":
        print("Game has drawn.")
    elif first_move.lower() == "scissors" and second_move.lower() == "rock":
        print(f"{player_two} has won.")
    else:
        print("Wrong Command. Try again.")

    print(" ")

    again = input("Do you want to play again? ")
    if again.lower() == "yes":
        print("")
        game()
    else:
        print("Thanks for playing!")
        exit()


game()
