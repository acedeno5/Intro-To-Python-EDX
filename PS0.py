# (----------- Indoor Voice --------------)

# Lowercasing everything that the user inputs

# InnerVoice = input(" Type Whatever you want! ").lower()

# print(InnerVoice)

# Finished



# (-------------- PlayBack Speed ----------)

# Inserting ... in between each spance

# PlayBack = input("Say a Sentence. We are going to Slow it Down for you. ").replace(" ", "...")

# print(PlayBack)

# Finished



# (--------------- Making Faces ---------------)

# implement a function called convert that accepts a str as input and returns that same input with any :) and returns an emoji instead


# def main():
   #  str = input("Say a sentence to change the some of the text to be emojified!")
   #  print(convert(str))
    
# def convert(str):
     # str = str.replace(":(","🙁").replace(":)", "🙂")
    # return str

# main()

#Finished





# (-------------- Einstein ----------------------)

#implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.

# Formula E = mc^2 

# def main():
    # m = int(input(" m: "))
    # print("Einstein Formula is", formula(m))
    
# def formula(n):
    # return n * (300000000 * 300000000)

# main()

#finished 

# Another way to do it 

# m = int(input("mass: "))
# c = 300000000
# e = m * c * c
# print(e)



# (-----------  Tip Calc -------------------)

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_without_dollar_sign = d.replace("$", "")
    return float(d_without_dollar_sign)


def percent_to_float(p):
    p_without_percent_sign = p.replace("%", "")
    p_converted = float(p_without_percent_sign) / 100
    return p_converted


main()

#FINISHED