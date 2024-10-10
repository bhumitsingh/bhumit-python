'''
Numbers
Types of Numbers
    -Python has various "types" of numbers (numeric literals).
    -Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
    -Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential
     (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to
     the power of 2) is also an example of a floating point number in Python.
Variable Assignment
    -We use a single equals sign to assign labels to variables. Let's see a few examples of how we can do this.
    -The names you use when creating these labels need to follow a few rules:
        -Names can not start with a number.
        -There can be no spaces in the name, use _ instead.
        -Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
        -It's considered best practice (PEP8) that names are lowercase.
        -Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
         or 'I' (uppercase letter eye) as single character variable names.
        -Avoid using words that have special meaning in Python like "list" and "str"
'''
# Basic Arithmetic

# Addition
sum1 = 2+1
print(sum1)
# Output 3

# Subtraction
difference1 = 2-1
print(difference1)
# Output 1

# Multiplication
product1 = 2*2
print(product1)

# Division
quotient1 = 3/2
print(quotient1)
# Output 1.5

# Floor Division
floorquotient1 = 7//4
print(floorquotient1)
# Output 1

# Modulo
remainder1 = 7%4
print(remainder1)
# Output 3

# Powers
value1 = 2**3
print(value1)
# Output 8

# Can also do roots this way
value2 = 4**0.5
print(value2)
# Output 2.0

# Order of operation followed in Python
value3 = 2 + 10 * 10 + 3
print(value3)
# Output 105

# Can use Parentheses to specify orders
value4 = (2+10)*(10+3)
print(value4)
# Output 156

# Use object names to keep better track of what's going on in your code!
my_income = 100
tax_rate = 0.1
my_tax = my_income * tax_rate

print(my_tax)
# Output 10.0