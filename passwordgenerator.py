import random

characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
              "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
              "!", "£", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "?"]

output = ""

password = input("How secure do you want your password to be? ")

if password.lower() == "weak":
    weak_password = random.sample(characters, 5)
    output = output.join(weak_password)
    print(output)
elif password.lower() == "medium":
    medium_password = random.sample(characters, 10)
    output = output.join(medium_password)
    print(output)
elif password.lower() == "strong":
    strong_password = random.sample(characters, 15)
    output = output.join(strong_password)
    print(output)
else:
    print("Please enter a password strength of weak, medium or strong.")
    exit()
