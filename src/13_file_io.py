"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
my_file = open("src/foo.txt")
print(my_file.readlines())
my_file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# with open("bar.text", mode="a+") as new_file:
#     text = new_file.writelines("This is a new file created with file IO.\n", "There are a few ways to write and read.\n", "To write you use mode=w and it will create a new file if one was not found")
#     print(text)
firsline = "This is a new file created with file IO. \n"
secondline = "There are a few ways to write and read. \n"
thirline = "To write you use mode=w and it will create a new file if one was not found"
text_file = open("bar.txt", "w")
text_file.write(f"{firsline}, {secondline}, {thirline}")
text_file.close()

try:
    with open("bar.txt",'r') as new_file:
        print(new_file.read())
except FileNotFoundError as err:
    print("file does not exist")
    raise err

