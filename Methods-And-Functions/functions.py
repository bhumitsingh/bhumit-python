"""
Functions
    -Formally, a function is a useful device that groups together a set of statements so they can be run more than once.
     They can also let us specify parameters that can serve as inputs to the functions.
def Statements
    - A def keyword is used to define a function in pyhon.
    - Syntax
        def name_of_function(arg1,arg2):
            '''
            This is where the function's Document String (docstring) goes
            '''
            # Do stuff here
            # Return desired result
"""

# Example 1 : A simple print 'hello' function
def say_hello():
    print('hello')

say_hello()

# Example 2 : A simple greeting function
def greeting(name):
    print('Hello %s' % name)

greeting('Bhumit')

# Using return

# Example 3 : Addition Function
def add_num(num1,num2):
    return num1+num2

add_num(4,5)

# Can also save as variable due to return
result = add_num(4,5)

print(result)

# Adding Strings
result2 = add_num('one','two')
print(result2)

def is_prime(num):
    '''
    Naive method of checking for primes.
    '''
    for n in range(2,num):
        if num % n == 0:
            print(num,'is not prime')
            break
    else: # If never mod zero, then prime
        print(num,'is prime!')

is_prime(16)
is_prime(17)