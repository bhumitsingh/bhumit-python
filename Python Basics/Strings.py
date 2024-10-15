"""
Strings
    -Strings are used in Python to record text information, such as names. Strings in Python are actually a sequence,
     which basically means Python keeps track of every element in the string as a sequence. For example, Python
     understands the string "hello" to be a sequence of letters in a specific order. This means we will be able to
     use indexing to grab particular letters (like the first letter, or the last letter).
"""
# Creating a String
word1 = 'Hello'
print(word1)

# Entire phrase
phrase1 = 'This is also a String'
print(phrase1)

# Using Double Quotes
phrase2 = "String built with double quotes"
print(phrase2)
'''
String Indexing : In Python, we use brackets [] after an object to call its index. We should also note that indexing
                  starts at 0 for Python.
'''
new_string = "Hello World!"
print(new_string)

# Show first Element
print(new_string[0])

# : can be used for slicing
print(new_string[:3])
print(new_string[4:])

# Grab everything, but go in step sizes of 2
print(new_string[::2])

# This can be used to print string backwards
print(new_string[::-1])

# String Properties

# Concatenate Strings
new_string = new_string + " How is everyone doing."
print(new_string)

# We can use the multiplication to create repetition
letter = "z"
print(letter)
letter = letter * 10
print(letter)

#Basic built-in String Methods

# Uppercase a String
print(new_string.upper())

# Lowercase a String
print(new_string.lower())

# Split a String by blank spaces
print(new_string.split())

# Split by a specific element
print(new_string.split("d"))

# Inserting a formated string
new_string = new_string + " {}"
print(new_string.format("My name is Bhumit Dev Singh."))