"""
Dictionaries
    -Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative
     position.
    -This is an important distinction, since mappings won't retain order since they have objects defined by a key.
"""

# Constructing a Dictionary

# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)

# Call values by their key
print(my_dict['key2'])

# It's important to note that dictionaries are very flexible in the data types they can hold. For example:
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict)

# Let's call items from the dictionary
print(my_dict['key3'])

# Can call an index on that value
print(my_dict['key3'][0])

# Can then even call methods on that value
print(my_dict['key3'][0].upper())

# Nesting Dictionaries

# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}

# Method to return a list of all keys
print(d.keys())

# Method to grab all values
print(d.values())