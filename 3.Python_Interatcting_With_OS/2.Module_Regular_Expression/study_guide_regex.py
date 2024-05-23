#!/usr/bin/python3

import re

# This pattern matches the number in the format 111-222-3333
pattern_1 = r"\d{3}-\d{3}-\d{4}"

print("Ex Matching the number in the follwing sentence")
print(re.search(pattern_1,"The number here in India 895-562-3693 is not valid"))

# This pattern matches positive or negative number, with or without decimal places
pattern_2 = r""
