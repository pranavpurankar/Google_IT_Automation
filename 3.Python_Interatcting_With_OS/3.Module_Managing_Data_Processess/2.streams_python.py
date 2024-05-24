#!/usr/bin/python3

'''
I/O streams
The basic mechanism for performing inputs and output operations in your program.
The mechanism behind how keyboard and screen is connected behind the scene.

How I/O streams works basically it is present everywhere even though when we type something on
our Linux terminal it works the same way. 
Input(Keyboard) --> [Program] --> Display

Types of I/O streams
standard input => STDIN
standard output => STDOUT
standard error => STDERR
'''

print("Streams in Python")
data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)
