"""
while Loops
    -The while statement in Python is one of most general ways to perform iteration.
    -A while statement will repeatedly execute a single statement or group of statements as long as the condition is true.
    -The reason it is called a 'loop' is because the code statements are looped through over and over again until the
     condition is no longer met.
    -Syntax:
        while test:
            code statements
        else:
            final code statements
"""
# Example 1
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1

# Example 2
x = 0

while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1
else:
    print('All Done!')

"""
break, continue, pass
    -We can use break, continue, and pass statements in our loops to add additional functionality for various cases. 
    -The three statements are defined by:
        break: Breaks out of the current closest enclosing loop.
        continue: Goes to the top of the closest enclosing loop.
        pass: Does nothing at all.
    - Syntax:
        while test: 
            code statement
        if test: 
            break
        if test: 
            continue 
        else:
"""

# Example 1
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('x==3')
    else:
        print('continuing...')
        continue

# Example 2
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue