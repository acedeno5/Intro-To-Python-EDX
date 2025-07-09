#------Unit Test---------


# This is Calc.py below

def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))
    
def square(n):
    return n * n

if __name__ == "__main__":
    main()
    
    
# test_calculator.py below

from calculator import square

def main():
    test_square()

""" def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9") """

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
            print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
        

#pytest third party library to test code
        
if __name__ == "__main__":
    main()
    
    
# New test using py test

from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    #assert square("cat") == 0

#pip install pytest.  (This is to use a python testing library)
# In terminal write pytest test_calculator.py



# updated test

import pytest
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
    
def test_str():
    with pytest.raises(TypeError):
        square("cat")
    

#hello.py below

def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()
    
#test for hello

from hello import hello

def test_default():
    assert hello() =="hello, world"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]: # Using loop to test arguments
        assert hello(name) == f"hello, {name}"
    #assert hello("David") == "hello, David"
    
# To test folder you need to create a __init__.py file 
