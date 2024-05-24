#!/usr/bin/env python3

'''
The sub process module offers a lot of extra options that we can 
use in our scripts. For example, we called out in an earlier video
that one way of providing information to our processes is to modify
the environment variables.

So in this code, we start by calling the copy method of the OS
environ dictionary that contains the current environment variables.
This creates a new dictionary that we can change as needed without
modifying the original environment.

The change that we're doing in this script is adding one extra
directory to the path variable. Remember, the path variable
indicates where the operating system will look for the executable
programs.

By adding one entry to the path, we're telling the OS to look for
programs in an additional location. To create the new value, we're
calling the join method on the OS path substring. This joins
elements of the list that we're passing with a path separator
corresponding to the current operating system.
'''

import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/",my_env["PATH"]])

result = subprocess.run(['myapp'],env=my_env)
print(type(result))
