"""
projekt_2.py: druhý projekt (Bulls and Cows) do Engeto Online Python Akademie

author: Karolína Wallenfelsová
email: wallenka@icloud.com
"""

# Bulls and Cows
# aim is to guess 4 digit generated number, where the digits can't repeat and first can't be 0
import random

number = []
chosen_number = ""
attempts = 0
cows = 0
bulls = 0

# list s cislama
# chci nahodne vytvorit cislo a pridat ho k listu, pokud tam jeste neni
# pokud je na indexu 0 0, musi vymyslet jine co neni nula

def underscore():
    print("-" * 47)
def generate_number():
    while len(number) < 4:
        x = random.randrange(0,9)
        if x not in number:
            number.append(x)
        if number[0] == 0:
            y = random.randrange(1,9)
            number.insert(0, y)
    print(number)

def game():
    global attempts
    global chosen_number
    attempts += 1  # adds number of attempts each turn
    cows = 0
    global bulls
    guess = []

    cows = 0
    bulls = 0
    chosen_number = "0"
    while len(chosen_number) != 4 or chosen_number.isnumeric() is False:
        print("Enter a number:")
        underscore()
        chosen_number = input(">>> ")
        if len(chosen_number) != 4:
            print("Enter a number that has 4 digits.")
        elif chosen_number.isnumeric() is False:
            print("Enter a valid number.")

    for i in range (4):
        guess.append(int(chosen_number[i]))
    for x in range (4):
        if guess[x] == number[x]:
            bulls += 1
        elif guess[x] in number and guess[x] != number[x]:
            cows += 1
    if bulls == 4:
        print(f"Correct, you've guessed the right number in {attempts} guesses!")
    elif bulls <4:
        print(f"{bulls} bulls, {cows} cows")

generate_number()
while bulls != 4:
    game() # jak udelat, aby to bylo v loopu
