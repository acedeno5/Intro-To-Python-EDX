#------ LIBRARIES --------

import statistics
import random
import sys
#from random import choice

coin = random.choice(["heads" , "tails"])
print(coin)

'''coin = choice(["heads" , "tails"]) # use this with the from statement
print(coin)'''


number = random.randint(1,10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
    
    

print(statistics.mean([100 , 90]))



""" try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
 """
 
""" if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is" , sys.argv[1]) """



if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")


print("hello, my name is" , sys.argv[1])




if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:
    print("hello, my name is" , arg)
    
    
    
# pip install (package name)

# Don't put the paranthesis around the package name it's just for me to show

# This line above is to install packages


import json
import requests # Got to install the package to use this

if lens(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent=2))
o = response.json()
for result in o["results"]:
    print(result["trackName"])
    
    

def main():
    hello("world")
    goodbye("world")
    
def hello(name):
    print (f"hello, {name}")

def goodbye(name):
    print (f"goodbye, {name}")
    
if __name__ == "__main__":
    main()


#from saying import goodbye  -> This is to create your own package and get the function