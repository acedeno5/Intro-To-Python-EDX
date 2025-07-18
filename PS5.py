# Testing my twtrr

#---- Just setting up my twttr----

def main():
    answer = input('Input: ')
    shorten(answer)


def shorten(word):
    vowels = ['a','e','i','o','u']

    for v in word:
        if v.lower() in vowels:
            word = word.replace(v, "")
    return word


if __name__ == '__main__':
    main()
import pytest
from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('CS50P') == 'CS50P'
    assert shorten('OrAnge') == 'rng'
    assert shorten('123') == '123'
    assert shorten('This is CS50P') == 'Ths s CS50P'
    assert shorten('Good Day !') == 'Gd Dy !'

if __name__ == "__main__":
    main()
#Submitted

# Back to the bank

from bank import value

def main():
    test_value()
    test_numbers()
    test_case()

def test_value():
    assert value('Hello') == 0
    assert value('Hello, Newman') == 0
    assert value("What's happening") == 100
    assert value("") == 100
    assert value('How are you doing?') == 20

def test_numbers():
    assert value('10') == 100
    assert value('200') == 100

def test_case():
    assert value('UPPER') == 100
    assert value('HELLO') == 0
    assert value('how are you') == 20
    assert value('welcome') == 100
    assert value('sUP dUde') == 100

if __name__ == "__main__":
    main()

#Submitted 


# Re-requesting a Vanity Plate
# (---------Vanity Plates---------------)
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    zero_index = s[2:].find('0')
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum() and zero_index != 0:
        if s[2:4].isdigit() and s[-1].isalpha():
            return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    main()

# Re-requesting a Vanity Plate
from plates import is_valid
import pytest

def main():
    test_length()
    test_first_two()
    test_space_punctuation()
    test_num_not_in_middle()

def test_length():
    assert is_valid('HELLO') == True
    assert is_valid('G') == False
    assert is_valid('GOODBYE') == False

def test_first_two():
    assert is_valid('HE') == True
    assert is_valid('05') == False
    assert is_valid('P1') == False

def test_space_punctuation():
    assert is_valid('HI, CS') == False
    assert is_valid('PI3.14') == False

def test_num_not_in_middle():
    assert is_valid('CS50P') == False
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

if __name__ == "__main__":
    main()

#Submitted




# Refueling

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            index = fraction.find("/")
            num = int(fraction[:index])
            den = int(fraction[index+ 1:])

            if (num/den) <= 1:
                percentage = round((num / den) * 100)
                return percentage
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return (str(percentage) + "%")

if __name__ == "__main__":
    main()

from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_for_errors()

def test_convert():
    assert convert("2/3") == 67
    assert convert("2/2") == 100
    assert convert("1/100") == 1

def test_gauge():
    assert gauge(67) == '67%'
    assert gauge(1) == 'E'
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'

def test_for_errors():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

if __name__ == "__main__":
    main()
 #Submitted



