#!/usr/bin/env python3

'''
Up to now, we've been using Python to interact with the operating system through
baked in functionality. For example, we've used file objects to read the contents of
files. Use the shutil module to check if the disk is full. And use a sys module to
process standard input, get parameters, or generate an exit code. But what if we
needed to run a system program from a Python script? Say, for example, that as part
of a Python script, we needed to send ICMP packets to a host to check if it's
responding.

We could try to look for an external module that provides this functionality. Or we
can just run the ping command, which will send packets for us. Sometimes it's easier
or faster to use a system command as part of our Python script to accomplish a task,
or use some functionality that doesn't exist in the Python modules, neither built in
or external. For these cases, Python provides a way to execute system commands in our
scripts, using functions provided by the subprocess module.
'''

import subprocess
subprocess.run(["date"])

print('''\nParent process blocked until child finishes it's work. Ex is sleep, it will
block the interpreter till it's finishes the child process that is sleep''')
subprocess.run(["sleep","2"])

print('''\n\nTill now we have seen the returncode=0. Let's checkout the returncode!=0.
If you want to see the returncode need to execute it on python3 interpreter. Let's check
out the file which is not present in the directory''')
result = subprocess.run(["ls","this_file_does_not_exist"])
print(result)


print('''You could do this with a script that calls the who command, which prints the users
currently logged into a computer.

The script could parse the output of the command, storing the list of logged-in users once 
per hour and at the end of the date to generate a daily report. To be able to process the 
output of commands, we'll set a parameter called capture output to true when calling the 
run function.

For our next example, we'll call the host command, which can convert a host name to an IP
address and vice versa.
When calling it, we'll pass the capture output equals true parameter and store the result 
in a variable so that we can access it.''')

result_1 = subprocess.run(["host","8.8.8.8"],capture_output=True)
print(result_1.returncode)
print(result_1.stdout)
print('''\nWhat is 'b' at the begining of string. That 'b' tells us that string is not a
proper string in the python. It's actually an array of bytes. This is little complex subject
read carefully: 
Data in computers is stored and transmitted in bytes and each can represent up to
256 characters. But there are thousands of possible characters out there used to 
write in various languages. Chinese, for example, requires over 10,000 different
characters. To be able to write in those languages, several specifications called
encodings have been created over time to indicate which sequences of bytes represent
which characters. Nowadays, most people use UTF-8 encoding, which is part of the 
Unicode standard that lists all the possible characters that can be represented. 

So going back to our example when we execute the command using run, Python doesn't
know which encoding to use to process the output of the command. So it simply 
represents it as a series of bytes. If we want this to become a proper string, 
we can call the decode method. This method applies an encoding to transform the
bytes into a string.

By default, it uses a UTF-8 encoding which is what we want. So with all that said,
let's transform our array of bytes into a string and then split it into several pieces.''')
print(result_1.stdout.decode().split())

print('''\nstderr:- If we use the capture output parameter and the command writes any 
output to standard error, it will be stored in the std or attribute of the completed 
process instance.''')

result_2 = subprocess.run(["rm","does_not_exists"],capture_output=True)
print("Printing_return_output: ",result_2.returncode)
print("stdout_was_empty: ",result_2.stdout)
print("stderr: ",result_2.stderr)
print("\nAbove is an excellent example of how stdout and stderr are different streams")


print(type(result_2))












