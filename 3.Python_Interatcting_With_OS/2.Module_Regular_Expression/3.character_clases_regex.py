#!/usr/bin/python3

import re
print(re.search(r"[Pp]ython","Python"))

print("\nCheck for expression from a-z")
print(re.search(r"[a-z]way","The end of the highway"))
print(re.search(r"[a-z]way","What a way to go"))

print("\nWe can combine many ranges as we want")
print(re.search(r"[a-zA-Z0-9]","The way ahead is littlecloudy"))
print(re.search(r"[a-zA-Z0-9]","The clubcloud9 is here"))

print("\nExclude something, lets create a searh pattern that filters that's not a letter using ^ circumflex")
print(re.search(r"[^a-zA-Z]","This is a sentence with spaces"))
print("Above example matched the first space. Now we don't want to match the space so added an extra space at the end of Z")
print(re.search(r"[^a-zA-Z ]","This is a sentence with spaces."))

print("\n\n\n| pipe character matches the either word either the word cat or dog")
print(re.search(r"cat|dog","I like cats."))
print(re.search(r"cat|dog","I like dog."))
print(re.search(r"cat|dog","I like cats and dogs"))

print("\nIn the above example we only get the first match findall module provides all the matches")
print(re.findall(r"cat|dog","I like both cats and dogs"))
