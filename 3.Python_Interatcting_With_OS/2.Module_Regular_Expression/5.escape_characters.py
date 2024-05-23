#!/usr/bin/python3

import re

# We want to match a string that has .com in it
print(re.search(r".com","Welcome"))
print("Above output is not what we want. It included the lcom. We need to include the escape character")

print(re.search(r"\.com","welcome"))
print(re.search(r"\.com","mydomain.com"))
print(re.search(r"\w*","Thos is an example"))
print(re.search(r"\w*","and_this is_another_4"))
