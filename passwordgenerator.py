'''
Password Generator
Write a programme, which generates a random password for the user. 
Ask the user how long they want their password to be, and how many letters and 
numbers they want in their password. Have a mix of upper and lowercase letters, 
as well as numbers and symbols. The password should be a minimum of 6 characters long.

Help From: https://pynative.com/python-generate-random-string/
'''

import random
import string
import os

def RandomCharacterString(stringLength=10):
    """Generate a random alpha string of fixed length """
    # all alpha characters
    letters = string.ascii_letters

    mystr = ""

    for i in range(stringLength):
        mystr = mystr + random.choice(letters)
        # Use random.sample(letters,stringLength) -- if you don't want repeats
        i = i + 1
    return mystr   

def RandomNumberString(stringLength=10):
    """Generate a random alpha string of fixed length """
    # all numbers characters
    numbers = string.digits

    mystr = ""

    for i in range(stringLength):
        mystr = mystr + random.choice(numbers)
        # Use random.sample(letters,stringLength) -- if you don't want repeats
        i = i + 1
    return mystr   

def RandomSymbolString(stringLength=10):
    """Generate a random alpha string of fixed length """
    # all alpha characters
    mysymbols = "!@*.$#"

    mystr = ""

    for i in range(stringLength):
        mystr = mystr + random.choice(mysymbols)
        # Use random.sample(letters,stringLength) -- if you don't want repeats
        i = i + 1
    return mystr   

def RandomizeMyPassword(mypassowrd):
    mystr = list(mypassowrd)
    random.shuffle(mystr)
    return ''.join(mystr)
    '''
    mynew= random.shuffle(mystr,len(mystr))
    print(mynew)
    '''

# Clear the Terminal Window to make things easier to read
os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to Kimmie's Password Generator")
print(" ")

password_length = 0
mystring=""

while password_length < 6:
    password_length = int(input("How long would your like your password to be (min. 6 characters): ").strip())

password_num_letters = int(input("How many letters do you wish to have: ").strip())
password_num_numbers = int(input("How many numbers do you wish to have: ").strip())

# Update the length of the requested password if numbers and letters requested
# is greater.
if password_num_letters + password_num_numbers > password_length:
    print("The number of letters and numbers requested exceeds the password length requested")
    print("Therefore updating password length to {}".format(password_num_letters + password_num_numbers))

# Symbols will only be used if the length of the password requested
# is greater than the number of numbers and letters requested.
if password_length > password_num_letters + password_num_numbers:
    print("The password length exceeds the number of letters and numbers requested.")
    print("Therefore your password will include {} symbols as well".format(password_length - password_num_letters - password_num_numbers))
    mystring = RandomSymbolString(password_length - password_num_letters - password_num_numbers)

mystring = mystring + RandomCharacterString(password_num_letters)
mystring = mystring + RandomNumberString(password_num_numbers)

print("Your new password is {}".format(RandomizeMyPassword(mystring)))