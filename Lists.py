"""
Lists:
    Lists can be thought of the most general version of a sequence in Python. Unlike strings, they are mutable, meaning
    the elements inside a list can be changed!
"""
from Strings import new_string

# Assign a list to a variable name my_list
my_list = ["A String",23,100.232,'o']
print(my_list)

# len() is used to print the length of the list
print(len(my_list))

# Indexing and Slicing
my_list = ["apple","oranges","milk","coconut"]
print(my_list)

# Grab element at index 0
print(my_list[0])

# Grab index 1 and everything past it
print(my_list[1:])

# Grab everything upto index 3
print(my_list[:3])

# '+' is used to concatenate lists
my_list = my_list + ['tomatoes']
print(my_list)
# '*' is used to multiply lists
print(my_list*2)

# Basic List Methods
list1 = [1,2,3]
print(list1)

# Use append method to permanently add an item to the end of a list:
list1.append('append me!')
print(list1)

# Pop method is used to pop off an item from the list
list1.pop()
print(list1)

# Sort and reverse methods can also be used effect your lists
new_list = ['a','e','x','b','c']
print(new_list)

# Use reverse to reverse order
new_list.reverse()
print(new_list)

# Use sort to sort a list
new_list.sort()
print(new_list)

# Nesting Lists
lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_3 = [7,8,9]

matrix = [lst_1,lst_2,lst_3]
print(matrix)

print(matrix[0])
print(matrix[0][1])