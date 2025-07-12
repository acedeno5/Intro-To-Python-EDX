#----- ET Cetera -----

#sets


#global

#bank.py
class Account:
    def __init__(self):
        self._balance = 0
        
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self,n):
        self._balance +=n
    
    def withdraw(self,n):
        self._balance -= n
    
def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)
    

if __name__ == "__main__":
    main()
        

#meows.py

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")
        
cat = Cat()
cat.meow()


#pip install mypy

#meows.py. but with the installation above

def meow(n: int) -> str:
    """
    Meow n times.
    
    :param n: Number of times to mewo
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n mewos, one per line
    :rtype:str
    
    """
    return "meow\n" * n
    
    
number: int  = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

#use in the terminal
# mypy meows.py


# Another update of meows.py

import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")
    

# Another update of meows.py

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help ="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")



#unpack.py

def total(galleons,sickles,knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100,"sickles": 50,"knuts":25}

print(total(**coins), "Knuts") # For list it's only one * before coins.. This is all to unpack


#another unpacked.py
def f(*args, **kwargs):
    print("Named:", kwargs)
    
    
f(galleons=100,sickles=50,knuts=25)

#yell
def main():
    yell(["This", "is", "CS50"])
    
def yell(*words):
    uppercased = map(str.upper, words)
    #uppercased = [word.upper() for word in words]   #List comprehension Style 
    print(*uppercased)
    
if __name__ == "__main___":
    main()
    

#filter
# example of filter filter(is_gryffindor, students)

#enumerate

#yield

#iterators

#say.py

import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
