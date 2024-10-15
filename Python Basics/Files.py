"""
Files
    -Python uses file objects to interact with external files on your computer.
    -These file objects can be any sort of file you have on your computer, whether it be an audio file, a text file, emails,
     Excel documents, etc.
     -You will probably need to install certain libraries or modules to interact with those various file types, but they are
      easily available.
     -Python has a built-in open function that allows us to open and play with basic file types.
"""

my_file = open('test.txt')
print(my_file.read())

# But what happens if we try to read it again?
print(my_file.read())
# This happens because you can imagine the reading "cursor" is at the end of the file after having read it.

# Seek to the start of file (index 0)
my_file.seek(0)
contents = my_file.read()
print(contents)

# Readlines returns a list of the lines in the file
my_file.seek(0)
print(my_file.readlines())

my_file.close()

# Writing to a file
# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file

my_file = open('test.txt', 'w+')

# Write to the file
my_file.write('This is a new line')
my_file.seek(0)
print(my_file.read())
my_file.close()