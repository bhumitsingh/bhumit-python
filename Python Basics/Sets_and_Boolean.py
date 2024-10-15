"""
Sets and Booleans
    -Sets are an unordered collection of unique elements. We can construct them by using the set() function.
    -Python comes with Booleans (with predefined True and False displays that are basically just the integers 1 and 0).
    -It also has a placeholder object called None.
"""

x = set()
# We add to sets with the add() method
x.add(1)
print(x)

# Add a different element
x.add(2)
print(x)

# Create a list with repeats
list1 = [1,1,2,2,3,4,5,6,1,1]

# Cast as set to get unique values
print(set(list1))

# Set object to be a boolean
a = True

# Output is boolean
print(1 > 2)

# None placeholder
b = None
print(b)