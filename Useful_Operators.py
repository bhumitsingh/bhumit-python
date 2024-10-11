"""
range
    -The range function allows you to quickly generate a list of integers, this comes in handy a lot, so take note of
     how to use it! There are 3 parameters you can pass, a start, a stop, and a step size.
"""
range(0,11)

# Notice how 11 is not included, up to but not including 11, just like slice notation!
list(range(0,11))
list(range(0,12))

# Third parameter is step size!
# step size just means how big of a jump/leap/step you
# take from the starting number to get to the next number.
list(range(0,11,2))
list(range(0,101,10))

"""
enumerate:
    -Keeping track of how many loops you've gone through is so common, that enumerate was created so you don't need to 
     worry about creating and updating this index_count or loop_count variable
"""

index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1

# Notice the tuple unpacking!

for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

"""
zip:
    -You can use the zip() function to quickly create a list of tuples by "zipping" up together two lists.
"""
list(enumerate('abcde'))

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

# This one is also a generator! We will explain this later, but for now let's transform it to a list
zip(mylist1,mylist2)

list(zip(mylist1,mylist2))

for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))

# in operator
var = 'x' in ['x', 'y', 'z']
print(var)
var = 'x' in [1, 2, 3]
print(var)

# min and max
mylist = [10,20,30,40,100]
minvalue = min(mylist)
print(minvalue)
maxvalue = max(mylist)
print(maxvalue)

# random - Python comes with a built-in random library. There are a lot of functions included in this random library
from random import shuffle
# This shuffles the list "in-place" meaning it won't return
# anything, instead it will affect the list passed
shuffle(mylist)

print(mylist)
from random import randint
# Return random integer in range [a, b], including both end points.
print(randint(0,100))

# Return random integer in range [a, b], including both end points.
print(randint(0,100))

# input
user_input = input('Enter Something into this box: ')
print(user_input)
