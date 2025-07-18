# Emojize
import emoji

user_answer = input("Input: ")

output = emoji.emojize(user_answer)

print("Output:",output)

#Solution that works
import emoji
x = input("Input: ")

print(emoji.emojize(f"Output:{x}", language='alias'))
#Submitted

# Frank, Ian and Glen's Letters
import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    sys.exit(1)
    
msg = input("Input: ")

#You can then get a list of available font with code like this:
figlet.getFonts()

msg = input("Input: ")

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())
    print(figlet.renderText(msg))
#submitted

# Adieu, Adieu

import inflect

p = inflect.engine()
# Create list to keep track of names
names = []
# Loop forever
while True:
    try:
        #Get user input
        name = input("Name: ")
        names.apppend(name)
    except EOFError:
        # Create new line and stop the loop
        print()
        break
#Printing using inflect module
output = p.join(names)
print ("Adieu, adieu, to " + output)
# Submitted


# Guessing Game
import random
# Get level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

# Set random number
random_number = random.randint(1,level)


#Get guess and check
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("too large!")
            else:
                print("Just right!")
                break
    except:
        pass

#submitted

# Little Professor

import random

def main():
    # Call get_level()
    level = get_level()
    # Get the score
    score = simulate_game(level)
    # Print
    print("Score: ", score)
    

def get_level():
    # Loop forever
    while True:
    # Get level and check if it is between 1 and 3
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level

def generate_integer(level):
    #Depending of the lvel, get a different random integer
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

# Simulate round(the math problem itself)
def simulate_round(x,y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x+y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

# Simulate game
def simulate_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x,y = generate_integer(level)
        response = simulate_round(x,y)
        if response == True:
            score += 1
        count_round += 1
    return score

if __name__ == "__main__":
    main()

#Solutuion with no errors
import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        tries = 0

        while tries < 3:
            try:
                answer = int(input(f"{X} + {Y} = "))
            except ValueError:
                print("EEE")
                tries += 1
                continue

            if answer == X + Y:
                score += 1
                break
            else:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{X} + {Y} = {X + Y}")

    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Please choose a valid level (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()

# Bitcoin Price Index


import requests
from sys import argv, exit
import os

# Check for proper command-line usage
if len(argv) != 2:
    exit("Missing command-line argument")

try:
    # Convert input to float (for number of bitcoins)
    bitcoins = float(argv[1])

    # Optional: load API key from environment variable
    api_key = os.getenv("affc229956489b481293313a2f6c1e70612e2035b1b556edfa044d5204dd7200")

    # Set up headers if API key exists
    headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

    # Make API request to CoinCap
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin", headers=headers)
    response.raise_for_status()  # Raise error for HTTP issues

    # Extract price in USD
    btc_price = float(response.json()["data"]["priceUsd"])

except ValueError:
    exit("Command-line argument is not a number")
except requests.RequestException:
    exit("Error fetching Bitcoin price")
except (KeyError, TypeError):
    exit("Error parsing API response")

# Print final result to 4 decimal places with commas
print(f"${bitcoins * btc_price:,.4f}")

