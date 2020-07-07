"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import fileinput
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
for arg in sys.argv:
    print("arguments: ",arg)

# Print out the OS platform you're using:
# YOUR CODE HERE
print("platform: ",sys.platform)
# Print out the version of Python you're using:
# YOUR CODE HERE
print("version:",sys.version_info)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
import os
print(os.path)
# Print the current process ID
# YOUR CODE HERE
print("process id: ", os.getpid())
print(os.ctermid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("Working directory: ",os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("login: ",os.getlogin())
