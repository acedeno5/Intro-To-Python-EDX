#(--------LOOPS------------)

# Cat.PY

# print("meow")
# print("meow")
# print("meow")

# -> Another way to do Meow with Loops

# i = 3 
# while i != 0:
    # print("Meow")
    # i = i - 1
    
# 3rd Way to do it with a loop

# i = 0
# while i < 3:
    # print("Meow")
    #i = i + 1
    #Same thing below and above
    # i += 1
    
# -> Lists (doing same thing as above with a list)

# for i in [0, 1, 2]:
#   print("meow")

        # -> Another way to do it with a list
# for _ in range(3):
   # print("meow")
   
# print ("meow\n" * 3, end="")

# ->  User input with Meow

# while True:
    # n = int(input("What's n? "))
    # if n > 0:
       #  break
    
# for _ in range(n):
    # print("meow")
    
# -> Doing with a main function

# def main():
    # number = get_number()
    # meow(number)
    
""" def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
        
def meow(n):
    for _ in range(n):
        print("meow")

main() """

# ----> Hogwarts now

""" students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2]) """

# -> Printing using a loop

""" students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student) """
    
# students = ["Hermione", "Harry", "Ron"]

""" for i in range(len(students)):
    print (i + 1, students[i]) """ 
#len for length in list
    
# students = ["Hermione", "Harry", "Ron" , "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# -> Dic = Dictionary

""" students = {
    "Hermione" : "Gryffindor", 
    "Harry" : "Gryffindor", 
    "Ron" : "Gryffindor", 
    "Draco" : "Slytherin"
}

for student in students:
    print(student, students[student], sep =" , ") """

""" print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])"""

# Composing a list of Dicts

""" students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ") """

# -> Mario
    # Nested Loops

# for _ in range(3):
   # print("#")
   
"""def main():
    print_column(3)
    
def print_column(height):
    print("#\n" * height, end="")
    # for _ in range(height):
       #  print("#")
        
main() """

"""def main():
    print_row(4)
    
def print_row(width):
    print("?" * width,)
   
        
main()""" 

def main():
    print_square(3)
    
""" def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print Brick
            print("#", end="")
        print()"""
        
def print_square(size):
    # For each row in square
    for i in range(size):
        # print("#" * size)
        print_row(size)

def print_row(width):
    print("#" * width)
   
        
main()

    







