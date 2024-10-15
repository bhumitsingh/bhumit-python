"""
map function
    - The map function allows you to "map" a function to an iterable object. That is to say you can quickly call the same
      function to every item in an iterable, such as a list.

filter function
    - The filter function returns an iterator yielding those items of iterable for which function(item) is true. Meaning
      need to filter by a function that returns either True or False. Then passing that into filter (along with your iterable)
      and you will get back only the results that would return True when passed to the function.

lambda expression
    - lambda expression allow us to create "anonymous" functions. This basically means we can quickly make ad-hoc functions.
      This basically means we can quickly make ad-hoc functions without needing to properly define a function using def.
"""
# Map Function
def square(num):
    return num**2

my_nums = [1,2,3,4,5]

print(list(map(square,my_nums)))

# the function can also be more complex
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]

my_names = ['Bhumit','Chamindi','Raj','Sachin','Priya']

print(list(map(splicer,my_names)))

# Filter Function
def check_even(num):
    return num%2 == 0

nums = [0,1,2,3,4,5,6,7,10]

print(list(filter(check_even,nums)))

# lambda expression

def square(num):
    result = num**2
    return result

print(square(4))

# this function could be simplified to

def square(num):
    return num**2

print(square(4))

# this could actually be written in one line as
def square(num): return num**2

print(square(4))

# this is the form of function that lambda intends to replicate. A lambda expression can be written as:

print(list(map(lambda num: num ** 2,my_nums)))