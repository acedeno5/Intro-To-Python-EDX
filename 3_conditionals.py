# (------Different ways of asking the same thing with conditionals----------------)

# x = int(input("What's x? "))
# y = int(input("What's y? "))

#-------Equal Equal

""" if x == y:
    print("x is not equal to y ")
else:
    print("x is equal to y ")
    """
    
    
#-------Not equal to

""" if x != y:
    print("x is not equal to y ")
else:
    print("x is equal to y ") """
    
# Using Or

""" if x < y or x > y:
    print("x is not equal to y ")
else:
    print("x is equal to y ") """
    
#---------elif and else

""" if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y") """
    
    
#(-------Doing your school Grade using Conditionals--------)

# score = int(input(" Score: "))

""" if score >= 90 and score <= 100:
    print(" Grade: A ")
elif score >= 80 and score < 90:
    print(" Grade: B ")
elif score >= 70 and score < 80:
    print(" Grade: C ")
elif score >= 60 and score < 70:
    print(" Grade: D ")
else:
    print(" Grade: F ") """
    
#----- Making the code Faster and more readible

""" if 90 <= score <= 100:
    print(" Grade: A ")
elif 80 <= score < 90:
    print(" Grade: B ")
elif 70 <= score < 80:
    print(" Grade: C ")
elif 60 <= score < 70:
    print(" Grade: D ")
else:
    print(" Grade: F ") """
    
""" if score >= 90:
    print(" Grade: A ")
elif score >= 80:
    print(" Grade: B ")
elif score >= 70:
    print(" Grade: C ")
elif score >= 60:
    print(" Grade: D ")
else:
    print(" Grade: F ") """
    
# (------------------Modulo Operator----------------)

# x = int(input(" What's x? "))

""" if x % 2 == 0:
    print(" Even ")
else:
    print( " Odd ") """ 
    
# Using a Function to do the same thing as above to determine an even or odd number

"""def main():
    x = int(input(" What's x? "))
    if is_even(x):
        print(" Even ")
    else: 
        print (" Odd ") """
        
# def is_even(n): 
    
    #One way to do it
    # if n % 2 == 0:
        # return True
    # else:
        # return False 
    
    # Another Way to do it
    
    # return True if n % 2 == 0 else False
    
    # Anonther way to do it
    
    # return n % 2 == 0 
    

    
# main()


# (--------- Match -----------)

name = input(" What's your name? ")

""" if name == "Harry" or name == "Hermione" or name == "Ron":
    print(" Gryffindor ")
elif name == "Draco":
    print(" Slytherin ")
else:
    print(" Who? ") """

#Going to improve it using Match 

""" match name:
    case "Harry":
        print(" Gryffindor ")
    case "Hermione":
        print(" Gryffindor ")
    case "Ron":
        print(" Gryffindor ")
    case "Draco":
        print(" Slytherin ")
    case _:
        print(" Who? ") """ 
        
# Improving this match case

match name:
    case "Harry" | "Hermione" | "Ron":
        print(" Gryffindor ")
    case "Draco":
        print(" Slytherin ")
    case _:
        print(" Who? ") 
       
   
    
    
    



    
    
