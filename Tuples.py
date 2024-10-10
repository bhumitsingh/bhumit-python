"""
Tuples
    -In Python tuples are very similar to lists, however, unlike lists they are immutable meaning they can not be changed.
    -You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar.
"""

# Constructing Tuples

# Create a tuple
t = (1,2,3)

# Check len just like a list
print(len(t))

# Can also mix object types
t = ('one',2)

# Show
print(t)

# Use indexing just like we did in lists
print(t[0])

# Slicing just like a list
print(t[-1])

# Basic Tuple Methods

# Use .index to enter a value and return the index
print(t.index('one'))

# Use .count to count the number of times a value appears
print(t.count('one'))

"""
Immutability
    -It can't be stressed enough that tuples are immutable.
    -Because of this immutability, tuples can't grow. Once a tuple is made we can not add to it.
    
When to use Tuples
    -You may be wondering, "Why bother using tuples when they have fewer available methods?" To be honest, tuples are not used 
     as often as lists in programming, but are used when immutability is necessary. If in your program you are passing around 
     an object and need to make sure it does not get changed, then a tuple becomes your solution. It provides a convenient 
     source of data integrity.
    -You should now be able to create and use tuples in your programming as well as have an understanding of their immutability.
"""