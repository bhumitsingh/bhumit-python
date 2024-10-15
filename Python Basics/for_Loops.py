"""
for Loops
    -A for loop acts as an iterator in Python; it goes through items that are in a sequence or any other iterable item.
     Objects that we've learned about that we can iterate over include strings, lists, tuples, and even built-in iterables
     for dictionaries, such as keys or values.
    -Syntax:
     for item in object:
        statements to do stuff
"""

# Example 1
list1 = [1,2,3,4,5,6,7,8,9,10]

for num in list1:
    print(num)

# Example 2
for num in list1:
    if num % 2 == 0:
        print(num)

for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')

# Example 3
# Start sum at zero
list_sum = 0

for num in list1:
    list_sum = list_sum + num

print(list_sum)

# Start sum at zero
list_sum = 0

for num in list1:
    list_sum += num

print(list_sum)

# Example 4
for letter in 'This is a string.':
    print(letter)

# Example 5
tup = (1,2,3,4,5)

for t in tup:
    print(t)

# Example 6
list2 = [(2,4),(6,8),(10,12)]

for tup in list2:
    print(tup)

# Now with unpacking!
for (t1,t2) in list2:
    print(t1)

# Example 7
d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item)

# Create a dictionary view object
d.items()

# Dictionary unpacking
for k,v in d.items():
    print(k)
    print(v)

list(d.keys())

sorted(d.values())