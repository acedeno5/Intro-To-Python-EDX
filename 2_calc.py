#  x = float(input("What's x? "))
#  y = float(input("What's y? "))

# (---------To Round Z to Nearest Int-----------)

#z = round(x + y)

#(-------- Divide X and Y and Round it with the built in Operator-----------)

# z =round(x / y, 2 )

#(-------------------- Dividing X and Y but a different approach------------)

# z = (x / y)

#( --------- Same Rounding thing but with floats to the second decimal place------)

# print(f"{z:.2f}")


#To change to US Numbering System aka use commas
# print(f"{z:,}")

# print(z)

# (--------------------Return Values---------------)

def main():
    x = int(input("What's x? "))
    print("x squared is", square (x))
    
# (-----One way to square it----)

# def square(n):
    #return n ** 2

# ** means to raise to power to
  
# (-----Another way to square it-----)
  
# def square(n):
    # return n * n

# (----------- Last way to Square it--------)

def square(n):
    return pow(n,2)
# First Number is the number being raised to the power of and the second is to what power

main()