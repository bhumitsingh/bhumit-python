# Module 5: Modules and Packages Assignments
## Lesson 5.1: Importing Modules
### Assignment 1: Importing and Using Modules
###Import the `math` module and use it to calculate the square root of 25 and the sine of 90 degrees.

import math
# Calculate the square root of 25
print(math.sqrt(25))  # 5.0
# Calculate the sine of 90 degrees
print(math.sin(math.radians(90)))  # 1.0


### Assignment 2: Aliasing Modules
###Import the `datetime` module with an alias and use it to print the current date and time.

import datetime as dt
# Print the current date and time
print(dt.datetime.now())

### Assignment 3: Importing Specific Functions
###Import the `randint` function from the `random` module and use it to generate a random integer between 1 and 100.

import random
random_number = random.randint(1, 100)
print(random_number)

### Assignment 4: Importing Multiple Functions
###Import the `sqrt` and `pow` functions from the `math` module and use them to calculate the square root of 16 and 2 raised to the power of 3.

from math import sqrt, pow
print(sqrt(pow(16,3))) 
print(sqrt(pow(2,3)))

### Assignment 5: Handling Import Errors
###Write code that attempts to import a non-existent module and gracefully handles the import error by printing an error message.

try:
    import non_existent_module
except ImportError as e:
    print(f"Error: {e}")


