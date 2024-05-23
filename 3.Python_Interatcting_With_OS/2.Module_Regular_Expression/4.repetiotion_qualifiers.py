#!/usr/bin/python3

'''
So far we've looked at how to match one specific character, a group of characters or even any character. Now we're going to check out how to match these characters several times. So we wanted to find the longest word in the string, or we wanted to find the host names in a log file by checking for a bunch of alphanumeric characters between brackets. We can do this using another interesting RegEx concept, repeated matches.
'''

import re

print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

print("\n\n+ and ?")
print(re.search(r"o+l+","goldfish"))
print(re.search(r"o+l+","goollgle"))

print("\n\n? We marked it as optional")
print(re.search(r"p?each","To each their own"))
print(re.search(r"p?each","I like peaches"))
