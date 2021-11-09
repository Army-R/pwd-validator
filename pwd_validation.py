#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:19:27 2021

@author: Army-R
"""
# Password validator
import getpass
from string import punctuation

print("""
The nex rules validates if your password is good enough:
    1- No spaces
    2- Length between 8 and 16 characters
    3- At least 1 special character
    4- Al least 1 number
    5- At least 1 uppercase

    \x1B[3mNote: To exit just type a number > 5\x1B[0m
""")
print()

success = "SUCCESS: The password"
error = "ERROR: The password"

def blanks(pwd):
    """ Validate if the password has no blanks on it """
    if " " in pwd:
        return f"{error} must not have spaces"
        print()
    else:
        return f"{success} has no blanks"
        print()

def length(pwd):
    """ Validates if the password has a length b/w 8 and 16 characters """
    if len(pwd) not in range(8, 17):
        return f"{error} must be between 8 and 16 characters"
        print()
    else:
        return f"{success} have between 8 and 16 characters"
        print()

def special(pwd):
    """ Validates if the password has at least 1 special character """
    special_char = [True for x in pwd if x in punctuation]
    if len(special_char) == 0:
        return f"{error} must have at least 1 special character"
        print()
    else:
        return f"{success} have at least 1 special character"
        print()

def number(pwd):
    """ Validates if the password has at least 1 number """
    num = any(x.isdigit() for x in pwd)
    if not num:
        return f"{error} must have at least 1 number"
        print()
    else:
        return f"{success} have at leas 1 number"
        print()

def uppercase(pwd):
    """ Validates if the password has at least 1 uppercase """
    capital = any(x.isupper() for x in pwd)
    if not capital:
        return f"{error} must have at least 1 uppercase"
        print()
    else:
        return f"{success} have at least 1 uppercase"
        print()

pwd = getpass.getpass("Enter the password: ")
print()

while True:
    print()
    rule = int(input("Which rule do you want to validate? Choose a number from the rule set: "))
    print()

    if rule == 1:
        print(blanks(pwd))
    elif rule == 2:
        print(length(pwd))
    elif rule == 3:
        print(special(pwd))
    elif rule == 4:
        print(number(pwd))
    elif rule == 5:
        print(uppercase(pwd))
    else:
        print("ERROR: No rule found")
        break
