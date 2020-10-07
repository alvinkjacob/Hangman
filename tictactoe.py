def start():
    for element in game:
        print(element)
    while game[0][0] & game[0][1] & game[0][2] & game[1][0] & game[1][1] & game[1][2] & game[2][0] & \
            game[2][1] & game[2][2] == 0 and game[0][0] & game[1][1] & game[2][2] != 1 and game[0][0] & \
            game[1][1] & game[2][2] != 2 and game[0][2] & game[1][1] & game[2][0] != 1 and game[0][2] & \
            game[1][1] & game[2][0] != 2 and game[0][0] & game[0][1] & game[0][2] != 1 and game[0][0] & \
            game[0][1] & game[0][2] != 2 and game[1][0] & game[1][1] & game[1][2] != 1 and game[1][0] & \
            game[1][1] & game[1][2] != 2 and game[2][0] & game[2][1] & game[2][2] != 1 and game[2][0] & \
            game[2][1] & game[2][2] != 2 and game[0][0] & game[1][0] & game[2][0] != 1 and game[0][0] & \
            game[1][0] & game[2][0] != 2 and game[0][1] & game[1][1] & game[2][1] != 1 and game[0][1] & \
            game[1][1] & game[2][1] != 2 and game[0][2] & game[1][2] & game[2][2] != 1 and game[0][2] & \
            game[1][2] & game[2][2] != 2:
        position_one = input(f"Where does {player_one} want to position your '1'? ")
        print(" ")
        if position_one == "1,1":
            game[0][0] = 1
        elif position_one == "1,2":
            game[0][1] = 1
        elif position_one == "1,3":
            game[0][2] = 1
        elif position_one == "2,1":
            game[1][0] = 1
        elif position_one == "2,2":
            game[1][1] = 1
        elif position_one == "2,3":
            game[1][2] = 1
        elif position_one == "3,1":
            game[2][0] = 1
        elif position_one == "3,2":
            game[2][1] = 1
        elif position_one == "3,3":
            game[2][2] = 1
        for element in game:
            print(element)
        rules()
        if game[0][0] and game[0][1] and game[0][2] and game[1][0] and game[1][1] and game[1][2] and game[2][0] and \
                game[2][1] and game[2][2] != "0":
            print("Game has tied. ")
            exit()

        position_two = input(f"Where does {player_two} want to position your '2'? ")
        print(" ")
        if position_two == "1,1":
            game[0][0] = 2
        elif position_two == "1,2":
            game[0][1] = 2
        elif position_two == "1,3":
            game[0][2] = 2
        elif position_two == "2,1":
            game[1][0] = 2
        elif position_two == "2,2":
            game[1][1] = 2
        elif position_two == "2,3":
            game[1][2] = 2
        elif position_two == "3,1":
            game[2][0] = 2
        elif position_two == "3,2":
            game[2][1] = 2
        elif position_two == "3,3":
            game[2][2] = 2
        for element in game:
            print(element)
        rules()
        if game[0][0] and game[0][1] and game[0][2] and game[1][0] and game[1][1] and game[1][2] and game[2][0] and \
                game[2][1] and game[2][2] != 0:
            print("Game has tied. ")
            exit()


def rules():
    if game[0][0] & game[1][1] & game[2][2] == 1:
        print(f"Winner is {player_one}.")
        exit()
    elif game[0][0] & game[1][1] & game[2][2] == 2:
        print(f"Winner is {player_two}.")
        exit()
    elif game[0][2] & game[1][1] & game[2][0] == 1:
        print(f"Winner is {player_one}.")
        exit()
    elif game[0][2] & game[1][1] & game[2][0] == 2:
        print(f"Winner is {player_two}.")
        exit()
    elif game[0][0] & game[0][1] & game[0][2] == 1:
        print(f"Winner is {player_one}.")
        exit()
    elif game[0][0] & game[0][1] & game[0][2] == 2:
        print(f"Winner is {player_two}.")
        exit()
    elif game[1][0] & game[1][1] & game[1][2] == 1:
        print(f"Winner is {player_one}.")
        exit()
    elif game[1][0] & game[1][1] & game[1][2] == 2:
        print(f"Winner is {player_two}.")
        exit()
    elif game[2][0] & game[2][1] & game[2][2] == 1:
        print(f"Winner is {player_one}.")
        exit()
    elif game[2][0] & game[2][1] & game[2][2] == 2:
        print(f"Winner is {player_two}.")
        exit()
    elif game[0][0] & game[1][0] & game[2][0] == 1:
        print(f"Winner is {player_one}.")
        exit()
    elif game[0][0] & game[1][0] & game[2][0] == 2:
        print(f"Winner is {player_two}.")
        exit()
    elif game[0][1] & game[1][1] & game[2][1] == 1:
        print(f"Winner is {player_one}.")
        exit()
    elif game[0][1] & game[1][1] & game[2][1] == 2:
        print(f"Winner is {player_two}.")
        exit()
    elif game[0][2] & game[1][2] & game[2][2] == 1:
        print(f"Winner is {player_one}.")
        exit()
    elif game[0][2] & game[1][2] & game[2][2] == 2:
        print(f"Winner is {player_two}.")
        exit()


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


print("Welcome to a game of 'Tic Tac Toe'!")
player_one = input("Enter Player One name: ")
player_two = input("Enter Player Two name: ")
print(" ")
print("Please enter the box you want to enter your 1 or 2 into, in the form of a coordinate e.g. 3,2 (row,column).")
print(" ")


start()
