#!/usr/bin/python3

import re
print(re.search(r"A.*a","Argentina"))
print(re.search(r"A.*a","Azerbaijan"))
print("\nMaking it more stricter")
print(re.search(r"^A.*a$","Azerbaijan"))
print(re.search(r"^I.*a$","India"))
print(re.search(r"^A.*a$","Austrilia"))

print("\n\nPattern matching")
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern,"_this_is_a_valid_variable_name"))
print(re.search(pattern,"this isn't a valid variable name"))
print(re.search(pattern,"my_variable1"))
print(re.search(pattern,"1out"))
