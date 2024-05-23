#!/usr/bin/env python3

import re

# r represents the rawstring
result = re.search(r"aza","plaza")
result_1 = re.search(r"aza","bazaar")
print(result)
print(result_1)

print(re.search(r"p.ng","Pangaea",re.IGNORECASE))
