# Fuel Gauge

# While forever
while True:
    #Get user input
    fuel = input("Fraction: ")
    try:
        #Try to split the fuel
        numerator, denominator = fuel.split("/")
        #Convert into integers
        new_numerator = int(numerator)
        new_denominator = int(denominator)
        #Calc the percentage
        f = new_numerator / new_denominator
        # Check if its less than 1 and stop the loop
        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
# Multiply Percentage by 100
p = int(f * 100)
# Check if percentage is less than 1, print E
if p < 1:
    print("E")
# Check if percentage is greater than 99, print F
elif p >= 99:
    print("F")
# Otherwise, print the %
else:
    print(f"{p}%")
    
    
#Solution that passes all the cases
def main():
    while True:
        try:
            car = input("Fraction: ")
            x, y = car.split("/")
            # Convert to integers
            x = int(x)
            y = int(y)
            # Reject negative or zero denominator or negative numerator
            if x < 0 or y <= 0:
                continue
            fuel = x / y
            if fuel <= 1:
                tank(fuel)
                break
        except (ValueError, ZeroDivisionError):
            pass


def tank(fuel):
    tank = round(fuel * 100)
    if tank <= 1:
        print("E")
    elif tank >= 99:
        print("F")
    else:
        print(f"{tank}%")

if __name__ == "__main__":
    main()


# Felipe's Taqueria
# Create a menu dictionary
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
#Set total_amount to 0
total_amount = 0
# Loop forever
while True:
    try:
        #Get user input
        item = input("Item: ").title()
        #Check if item is already in the dictionary
        if item in menu:
            #add the item price to total_amount
            total_amount +=menu[item]
            # Print the current total_amount
            print("Total: $",end="")
            print("{:.2f}".format(total_amount))
    except EOFError:
        # Print a new line and stop the loop
        print()
        break

#submitted and finished

# Grocery List
# Create empty dictionary
grocery = {}
#Loop forever
while True:
    try:
        #Get user input
        item = input()
        #Check if item is already in the dictionary
        if item in grocery:
            #If it is, add 1 to the count
            grocery[item] += 1
        #otherwirse, add the item for the first time
        else:
            grocery[item] = 1
    except EOFError:
        # Print all the items in alphabetical order
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        #stop the while loop
        break
    
#Submitted and finished 


# Outdated

# Create list with the name of all months
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

# Loop forever
while True:
    # Get user input
    date = input("Date: ")
    try:
        #Split the date by /
        month, da, year = date.split("/")
        # Check if month is in between of 1 and 12 and day between 1 and 31
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            # Split the date by space
            old_month, old_day, year = date.split(" ")    
            # Find the number of the month
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1
                if not old_day.endswith(","):
                    continue
            # Remove comma from day variable
            day = old_day.replace(",","") # This is line 35
            # Check if month is in between of 1 and 12 and day between 1 and 31
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            #Go to the next line
            print()
            pass
        
#If month is less than 10, add a 0 before
# if day is less than 10, add a 0 before
# Print the result
print(f"{year}-{int(month):02}-{int(day):02}")
    
#Solution that actually works

# Create dictionary with the name of all months
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

# Loop forever
while True:
    # Get user input
    date = input("Date: ").strip()
    try:
        # Split the date by /
        month, day, year = date.split("/")
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
            break
    except:
        try:
            # Split the date by space
            old_month, old_day, year = date.split(" ")
            if old_month in months and old_day.endswith(","):
                month = months[old_month]
                day = old_day.replace(",", "")
                if (1 <= int(day) <= 31):
                    break
        except:
            pass

# Print the result
print(f"{year}-{int(month):02}-{int(day):02}")


