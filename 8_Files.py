# --------File I/O--------- 

#names.py below

names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")
    

#update

name = input("What's your name? ")

with open("names.txt", "a") as file:
#file = open("names.txt", "a") # w is write and a is append
    file.write(f"{name}\n")
#file.close()

#update 2

with open("names.txt", "r") as file:
    for line in file:
        print("hello, ", line.rstrip())
        
#update 3

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names): #reverse = True -> this nakes it reverses. You can put this with a comma after names in this line
    print(f"hello, {name}")

    
#names.csv is to keep track of a 2D file

#students.csv below

Hermoine,Gryffindor
Harry,Gryffindor
Ron,Gryffindor
Draco,Slytherin

#Updates students.csv for latest iteration below
name,home
Harry,"Number Four,Privet Drive"
Ron,The Burrow
Draco,Malfoy Manor

#students.py below

""" with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}") """ # Same thing as below but we are making it more readable below
        
        
with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        
        
#update of Students.py to sort it

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house":house}
        students.append(student)

def get_name(student):
    return student["name"]

        
for student in sorted(students,key=get_name):
    print(f"{student['name']} is in {student['house']}")
    
    
#Doing the same thing above but using lambda

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house":house}
        students.append(student)

       
for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")



#Updated Student.py for the updated students.csv
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.appennd({"name" : row["name"], "home" : row["home"]})

       
for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
    
    
#students.csv for the students.py below
name,home
    
#Another updated Students.py for csv above
import csv
name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home":home})


#Images,PIL Library

#costume1.gif
#costume2.gif

#costumes.py
import sys

from PIL import Image

images = []
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
    
images[0].save(
    "costumes.gif", save_all = True, append_images=[images[1]], duration=200,loop=0
)

#costumes.gif -> This should show a gif of a cat running 
