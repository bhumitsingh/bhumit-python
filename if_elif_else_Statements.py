"""
if, elif, else Statements
    -if Statements in Python allows us to tell the computer to perform alternative actions based on a certain set of results.
    -syntax:
        if case1:
            perform action1
        elif case2:
            perform action2
        else:
            perform action3
"""
if True:
    print('It was true!')

x = False
if x:
    print('x was True!')
else:
    print('I will be printed in any case where x is not true')

# Multiple Branches
loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the Auto Shop!')
elif loc == 'Bank':
    print('Welcome to the bank!')
else:
    print('Where are you?')

person = 'Sammy'

if person == 'Sammy':
    print('Welcome Sammy!')
else:
    print("Welcome, what's your name?")

person = 'George'

if person == 'Sammy':
    print('Welcome Sammy!')
elif person =='George':
    print('Welcome George!')
else:
    print("Welcome, what's your name?")