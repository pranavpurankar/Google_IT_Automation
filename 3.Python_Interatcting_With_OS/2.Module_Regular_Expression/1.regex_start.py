#!/usr/bin/env python3
'''
We want to fetch the information of the process. Which process ID is causing the trouble.
'''

log = "July 31 07:51:48 mycomputer bad_process[123456]:ERROR Performing package update"

# One method to extract the characters is Indexing
index = log.index("[")
print(log[index+1:index+6])

# Instead of using string method we will use regex
import re
regex = r"\[(\d+)]"
result = re.search(regex,log)
print(result)
