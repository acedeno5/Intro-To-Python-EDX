# Problem Set 2 for Loops

# (---------CamelCase---------------)

# Get user input
"""camelCase = input("camelCase: ")


# Print "snake_case:"
print("snake_case: ", end = "")

# Loop through every letter
for letter in camelCase:


# Check if letter is upper case
    if letter.isupper():
    # Print underscores and the letter in lowercase
        print("_" + letter.lower(), end="")
# Otherwise, print letter
    else:
        print(letter, end ="")

# Print Space in the end
print()"""
#Finished
#submitted

# (---------Coke Machine---------------)


"""# Variable to keep track
amount_due = 50
        

#Loop until amount_due is greater than 0
while amount_due > 0:
    #Print the amount due
    print("Amount Due: ", amount_due)
    #Ask user to insert coin
    coin = int(input("Insert Coin: "))
    #Check if coin is 25,10 or 5 cents
    if coin in [25,10,5]:
        #Subtract value from amount_due
        amount_due -= coin
        
#Calculate change_owed
change_owed = abs(amount_due)
#Print result
print("Change Owed: ", change_owed)"""

#Finished
#submitted

# (---------Just setting up my twttr---------------)
# Get the user's input
answer = input("Input: ")
#Print "Output"
print("Output: ", end = "")

# Loop through every letter
for letter in answer:
    #Check if it is not vowels whether inputted in upper case or lowercase
    if not letter.lower() in ['a','e','i','o', 'u']:
        #Print the letter
        print(letter,end="")
#Print new line
print()

#Finished and Submitted

# (---------Vanity Plates---------------)
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # vanity plates may contain a maxium of 6 character (letters or numbers) and a min of 2 characters (letters or numbers)
    if len(s) < 2 or len(s) > 6:
        return False
    # All vanity plates must start with at least two letter
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    # Numbers can't be used in the middle of the plate and must come at the end
    # The first number can't be a '0'
    number_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            if number_started == False:
                if s[i] == '0':
                    return False
                number_started = True
        elif number_started:
            # A letter appears after number has started
            return False
    # No periods, spaces, or punctation marks are allowed
    for c in s:
        if not c.isalnum():
            return False
    # If we pass all the tests, return True
    return True


main()

#Finished and Submitted


# (---------Nutrition Facts---------------)

#Create dictionary with all fruits and its calories
fruits = {
    "apple" : "130",
    "avocado" : "50",
    "banana" : "110",
    "cantaloupe" : "50",
    "grapefruit" : "60",
    "grapes" : "90",
    "honeydew melon" : "50",
    "kiwifruit" : "90",
    "lemon" : "15",
    "lime" : "20",
    "nectarine" : "50",
    "orange" : "80",
    "peach" : "60",
    "pear" : "100",
    "pineapple" : "50",
    "plums" : "70",
    "strawberries" : "50",
    "sweet cherries" : "100",
    "tangarine" : "50",
    "water melon" : "80"
}

# Get user input
fruit_asked = input("Item: ")
# loop through fruits dictionary
for key in fruits:
    # Find the fruit asked (remember to use lowercase)
    if key in fruit_asked.lower():
        # Print fruit's calories
        print("Calories:",fruits[key])