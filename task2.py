import random

import string

print("Hello, Welcome to HNG Tech boarding.")
print("We would a few details to get you setup, Thank you!")

# Gets the details of the user
first_name = input("Please enter your first name:  ")
last_name = input("Please enter your last name:  ")
email = input("please enter email address: ")

# Store the details in a dictionary
user_details = {
    "first_name" : first_name,
    "last_name" : last_name,
    "email" : email
}

# Get two letters from each of the names
first_two_chars = first_name[:2]
last_two_chars = last_name[-2:]

def randomString(stringLength=5):
    """Generate a random string."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

password = first_two_chars + last_two_chars + randomString() #Add all the characters
print(f"your password is {password}")

satisfaction = input("Are you okay with password? (Yes/No) ").lower()
while satisfaction == "no":
        password = input("Choose your password with 7 characters or more: ")
        if len(password) < 7:
            print("Try using a password that is more than 7 characters")
        else:
            break

print(user_details)
