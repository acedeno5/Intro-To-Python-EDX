#------Regular Expressions------


#Validate.py

email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid") 
    

#Updated Validate.py
import re

email = input("What's your email? ").strip()

if re.search(r"^(\w|\.)\w+@(\w+\.)?\w+\.edu$",email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
    
    

#format.py
import re

name = input("What's ypur name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + "" + matches.group(1)
print(f"hello, {name}")


#twitter.py

#re.sub is one that was mentioned
import re
url = input("URL: ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

#re.split
#re.findall



