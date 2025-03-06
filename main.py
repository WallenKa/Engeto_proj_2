"""
projekt_2.py: druhý projekt (Bulls and Cows) do Engeto Online Python Akademie

author: Karolína Wallenfelsová
email: wallenka@icloud.com
"""

# Bulls and Cows
# aim is to guess 4 digit generated number, where the digits can't repeat and first can't be 0
import random
import textwrap

# prints underscores so the code isn't cluttered with prints
def underscore():
    print("-" * 47)

# generates a random 4 digit number, where numbers can't repeat and the 1st digit is not 0
def generate_number():
    number = []
    while len(number) < 4:
        x = random.randrange(0,10)
        if x not in number:
            number.append(x)
        if number[0] == 0:
            y = random.randrange(1,10)
            number.insert(0, y)
    return number

# defines game, takes generated number and attempts
def game(number, attempts):
    guess = []
    cows = 0
    bulls = 0
    attempts += 1 # adds an attempt with every run
    chosen_number = "0"
    while len(chosen_number) != 4 or chosen_number.isnumeric() is False:  # checks if user entered number is correct
        print("Enter a number:")
        underscore()
        chosen_number = input(">>> ")
        if len(chosen_number) != 4:
            print("Enter a number that has 4 digits.")
        elif not chosen_number.isnumeric():
            print("Enter a valid number.")

    # convert user input string number into list of integers
    guess = [int(c) for c in chosen_number]

    for x in range(4):
        if guess[x] == number[x]:
            bulls += 1
        elif guess[x] in number and guess[x] != number[x]:
            cows += 1
    if bulls == 4:
        if attempts == 1:
            print(f"Correct, you've guessed the right number\nin {attempts} guess!")
        else:
            print("Correct, you've guessed the right number\n", textwrap.fill(f"in {attempts} guesses!", 47), sep="")
        underscore()
        print("That's amazing!")
    else:
        print(f"{bulls} bulls, {cows} cows")
    return attempts, bulls

# tohle ma byt ve fc main
number = generate_number()
attempts = 0
bulls = 0
print("Hi there!")
underscore()
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
underscore()
while bulls != 4:
    attempts, bulls = game(number, attempts)


