#!/usr/bin/env python3

import sys
print(sys.argv)

print("Exit status: The value returned by a program to the shell.")

print("\n\n This checks whether the file exists or not")

import os
filename=sys.argv[1]

if not os.path.exists(filename):
    with open(filename,"w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)
