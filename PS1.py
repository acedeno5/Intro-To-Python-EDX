# Problem Set 1 for Conditionals

# (---------Deep Thought---------------)

# Step 1. Get user input

# answer = input("What is the answer to the Great Question of Life,the Universe and Everything? ")

# Step 2. Print Yes if the user inputs 42 or (case-insentively) forty-two or forty two

# if answer.strip() == "42":
    # print("Yes")
# elif answer.lower().strip() == "forty-two":
    # print("Yes")
# elif answer.lower().strip() == "forty two":
   #  print("Yes")

# Step 3. Otherwise ouput No.

# else: print("No")

#Finished
#submitted


#(---------Home Federal Savings Bank-----------)

# Step 1 - Get user input

# answer = input("Greeting: ")

# new_answer = answer.lower().strip()

# Step 2 - Check is the answer has 'hello'

# if 'hello' in new_answer:
    # print("$0")

# Step 3 - Check if answer starts with 'h'
# elif 'h' == new_answer[0]:
    # print("$20")

# Step 4- Otherwise $100

# else:
# print("$100")
    
    #Finished
    #submitted

# (--------File Extensions-----------------------)

#Step 1 - Get user Input

#filename = input("File Name: ")

#new_filename = filename.lower().strip()

#Step 2 - Remove spaces and make it all lower

#Step 3 - If Gif or png or jpg or jpeg, print "image/type"

#if '.gif' in new_filename:
    #print("image/gif")
# elif '.png' in new_filename:
   #  print("image/png")
# elif '.jng' in new_filename:
   #  print("image/jng")
# elif '.jpeg' in new_filename:
    # print("image/jpeg")
#If Pdf or zip print "application/type"
# elif '.pdf' in new_filename:
   #  print("application/zip")
# elif '.zip' in new_filename:
    # print("application/zip")


#Step 4 - If txt, print "text/plain"
# elif '.txt' in new_filename:
   #  print("text/plain")

#Otherwise, print "application/ octet-stream"
# else:
    # print("application/ octet-stream")
    
# Finished
#submitted

#(------------Math Interpreter---------------------)

# Get user input

# expression = input("Expression: ")

# Convert this into variables

# x,y,z = expression.split(" ")

# Change type of variables x and z to float

# new_x = float(x)
# new_z = float(z)

# Calculate the result

# if y == "+":
    # result = new_x + new_z
# if y == "-":
    # result = new_x - new_z
# if y == "*":
    # result = new_x * new_z
# if y == "/":
    # result = new_x / new_z
# print(round(result, 1))

#Finished 

#submitted


#(---------------Meal Time-----------------------)

def main():
    # Get time from user
    
    answer = input("What's the time? ")
    
    #Call the convert function
    time = convert(answer)
    
    #breakfast between 7:00 and 8:00
    if time >= 7 and time <= 8:
        print("Breakfast time")
    
    #lunch between 12:00 and 13:00
    if time >= 12 and time <= 13:
        print("Lunch time")
    
    #dinner between 18:00 and 19:00
    if time >= 18 and time <= 19:
        print("Dinner time")


def convert(time):
    # Get hour and minute
    hours, minutes = time.split(":")
    #Convert time into a float number
    new_minute = float(minutes) / 60
    # Return the result to main function
    return float(hours) + new_minute
    
if __name__ == "__main__":
    main()
    
#Finished 
#submitted