# Seasons of Love
from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        year, month, day = [int(x) for x in input('Date of Birth: ').split('-')]
    except ValueError:
        sys.exit('Invalid Date')

    dob = check_birthdate(year, month, day)
    diff_minutes = calculate_diff(dob)
    words = p.number_to_words(diff_minutes, andword='')
    print(words.capitalize() + ' minutes')

def check_birthdate(year, month, day):
    try:
        dob = date(year, month, day)
    except:
        return 'Invalid Date'
    return dob

def calculate_diff(dob):
    return str(((date.today() - dob).days) * 24 * 60)

if __name__ == '__main__':
    main()

from seasons import *
import pytest

def main():
    test_check_birthdate()
    test_calculate_diff()

def test_check_birthdate():
    assert check_birthdate(2024,2,22) == date(2024,2,22)
    assert check_birthdate(22,2,2024) == 'Invalid Date'

# date of upload 11-April-2024. The difference need to be calculated accordingly
def test_calculate_diff():
    assert calculate_diff(date(2024,4,10)) == '1440'
    assert calculate_diff(date(1947,8,15)) == '40318560'


if __name__ == '__main__':
    main()
#Submitted


# Cookie Jar
class Jar:
    def __init__(self, capacity = 12):
        if capacity < 0:
            raise ValueError('Capacity cannot be negatve')
        self._capacity = capacity
        self._size = 0 # the underscore before size makes it kind of private & cannot be accessed outside the class

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        if n > self.capacity or n + self._size > self.capacity:
            raise ValueError('Trying to put in more than the capacity')
        self._size += n

    def withdraw(self, n):
        if n > self.capacity or n > self._size:
            raise ValueError('Cannot withdraw more than the capacity')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

import pytest
from jar import Jar

def test_init():
    jar_1 = Jar()
    jar_2 = Jar(5)
    assert jar_1.capacity == 12
    assert jar_1.size == 0
    assert jar_2.capacity == 5
    assert jar_2.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(1)
    assert str(jar) == '🍪'
    jar.deposit(11)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(4)
    assert jar.size == 7

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(2)
    assert jar.size == 10
    jar.withdraw(5)
    assert jar.size == 5

if __name__ == '__main__':
    main()


#Submitted

# CS50 Shirtificate

# CS50 Shirtificate
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 15, 70, 190)
        self.set_font("helvetica", "",30)
        # Printing title:
        self.cell(150, 10, "CS50 Shirtificate", border=0, align="C")


def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255,255,255)
    pdf.cell(-100, 213, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == '__main__':
    main()
    
#Submitted