#(-------Exceptions--------)

print("hello, world")

x = int(input("What' s x?"))
print(f"x is {x}")

#----Step 1----
try:
    x = int(input("What' s x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
    

#---- Step 2-----
    
    
while True:
    try:
        x = int(input("What' s x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")


# Another way to do it
while True:
    try:
        x = int(input("What' s x?"))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")


#---Step 3--


def main():
    x = get_int(" What's x? ")
    print(f"x is {x}")

""" def get_int():
    while True:
        try:
            x = int(input("What' s x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x """
    
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass # Means it won't say anything

main()




    

