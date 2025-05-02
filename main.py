"""
projekt_2.py: druhý projekt (Bulls and Cows) do Engeto Online Python Akademie

author: Karolína Wallenfelsová
email: wallenka@icloud.com
"""

# Bulls and Cows
# aim is to guess 4 digit generated number, where the digits can't repeat and first can't be 0
import random
import textwrap

def underscore():
    """Print underscores according to example output from Engeto Portal."""
    print("-" * 47)


def generate_number():
    """Generate a random 4 digit number.
    The digits cannot repeat and the first digit is not 0.
    """
    number = []
    while len(number) < 4:
        x = random.randrange(0,10)
        if x not in number:
            number.append(x)
        if number[0] == 0:
            y = random.randrange(1,10)
            number.insert(0, y)
    return number

def game(number, attempts):
    """Defines main part of game.
    Takes number and attempts,
    returns updated number of attempts and number of bulls.
    """
    guess = []
    cows = 0
    bulls = 0
    attempts += 1 # adds an attempt with every run
    chosen_number = "0"
    while len(chosen_number) != 4 or not chosen_number.isnumeric():  # checks if user entered number is correct
        print("Enter a number:")
        underscore()
        chosen_number = input(">>> ") # inputs digits from user
        if len(chosen_number) != 4:  # checks if user input matches the generated number
            print("Enter a number that has 4 digits.")
        elif not chosen_number.isnumeric():
            print("Enter a valid number.")
    # convert user input string number into list of integers
    guess = [int(c) for c in chosen_number]
    # guessing part of the game
    # if guessed number is correct and in correct position, add a bull
    # if correct and not in the correct position, add a cow
    for x in range(4):
        if guess[x] == number[x]:
            bulls += 1
        elif guess[x] in number and guess[x] != number[x]:
            cows += 1
    if bulls == 4:  # winning condition
        if attempts == 1:
            print(f"Correct, you've guessed the right number\nin {attempts} guess!")
        else:
            print("Correct, you've guessed the right number\n", textwrap.fill(f"in {attempts} guesses!", 47), sep="")
        underscore()
        print("That's amazing!")
    else:
        print(f"{bulls} bulls, {cows} cows")
    return attempts, bulls

def main ():
    number = generate_number()
    attempts = 0
    bulls = 0
    print("Hi there!")
    underscore()
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    underscore()
    while bulls != 4:  # while number is not guessed yet, pass attempts and bulls into game function
        attempts, bulls = game(number, attempts)

# execute main code
if __name__ == "__main__":
    main()