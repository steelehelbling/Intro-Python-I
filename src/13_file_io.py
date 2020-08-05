"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# # YOUR CODE HERE
# The first argument is a string containing the filename.
#  The second argument is another string containing a few 
# characters describing the way in which the file will be 
# used. mode can be 'r' when the file will only be read, 
# 'w' for only writing (an existing file with the same name 
# will be erased), and 'a' opens the file for appending; any
#  data written to the file is automatically added to the end. 
# 'r+' opens the file for both reading and writing. The mode 
# argument is optional; 'r' will be assumed if it’s omitted.

x = open("src/foo.txt", "r")
print(x.read())
x.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
y = open("src/bar.txt", "w")
y.write("first arbitrary content,")
y.write(" second arbitrary content,")
y.write(" three arbitrary content")
y.close()
z = open("src/bar.txt", "r")
print(z.read())
z.close()