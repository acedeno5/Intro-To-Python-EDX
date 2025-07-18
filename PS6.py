# Lines of Code
import sys

if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
    try:
        with open(sys.argv[1]) as file:
            count = 0
            for line in file:
                if not line.lstrip().startswith("#") and line.strip() != "":
                    count += 1
            print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith != ".py":
    sys.exit("Not a Python file")
    
#Submitted

#Pizza Py

import tabulate, sys, csv

if len(sys.argv) == 2 and sys.argv[1].endswith('.csv'):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            print(tabulate.tabulate(reader, headers = "keys", tablefmt='grid'))
    except FileNotFoundError:
        sys.exit('File does not exist')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif sys.argv[1].endswith != '.csv':
    sys.exit('Not a CSV file')
    
#Submitted

# Scourgify
import sys, csv

if len(sys.argv) == 3 and sys.argv[1].endswith('.csv'):
    try:
        with open(sys.argv[1],'r') as input_file:
            reader = csv.DictReader(input_file)
            with open(sys.argv[2],'w') as output_file:
                writer = csv.DictWriter(output_file, fieldnames= ['first','last','house'])
                writer.writeheader()
                for row in reader:
                    l_name, f_name = row['name'].split(',')
                    writer.writerow({'first':f_name.lstrip(),'last':l_name,'house':row['house']})
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
else:
    sys.exit('Not a CSV file')

#Submitted

#CS50 P-Shirt

import sys, os
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    extention = ['.jpg','.jpeg','.png']
    ext1 = os.path.splitext(sys.argv[1])
    ext2 = os.path.splitext(sys.argv[2])

    if ext1[1].lower() == ext2[1].lower() and ext1[1] in extention:
        try:
            user_image = Image.open(sys.argv[1],'r')
        except FileNotFoundError:
            sys.exit('Input does not exist')

        shirt = Image.open('shirt.png')
        size = shirt.size
        user_image = ImageOps.fit(user_image, size)
        user_image.paste(shirt, shirt)
        user_image.save(sys.argv[2])
    elif ext2[1].lower() not in extention:
        sys.exit('Invalid output')
    elif ext1[1].lower() != ext2[1].lower() and ext1[1].lower() in extention:
        sys.exit('Input and output have different extensions')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

#Submitted

    

