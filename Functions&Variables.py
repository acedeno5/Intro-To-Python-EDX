#( -----Ask user for their name-------)

# name = input("What's your name? ").strip().title()

# (------Remove Whitespace from String and Capitalize it-------)

# name = name.strip().title()

#(--------Split User's name into first and last name--------)

# first, last = name.split()

#(---------Say Hello to User---------)

# print(f"Hello, {first}")

"""
This is a multi line comemnt
You SEE!
"""

#(--------Defining a Function to Say Hello World and create a Paramter and return function with Name--------)

# def hello(to = "world"):
    # print("hello,", to)
    
# hello()
# name = input("What's your Name? ")
# hello(name)


# (-------Defining a Function to Say Hello World by Defining Main and Def Hello to do the same thing as above---------)

def main(): 
    name = input("What's your Name? ")
    hello(name)

def hello(to = "world"):
    print("hello,", to)

main()