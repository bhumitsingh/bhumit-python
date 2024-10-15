"""
*args
    -When a function parameter starts with an asterisk, it allows for an arbitrary number of arguments, and the function
     takes them in as a tuple of values.
**kwargs
    -Similarly, Python offers a way to handle arbitrary numbers of keyworded arguments. Instead of creating a tuple of
     values, **kwargs builds a dictionary of key/value pairs.
"""
def myfunc(a,b):
    return sum((a,b))*0.05 # returns 5% of sum of two numbers

print(myfunc(40,60))

def myfunc2(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*.05

print(myfunc2(40,60,20))

# Creating func2 using *args
def myfunc3(*args):
    return sum(args)*.05

print(myfunc3(10,20,70,40,60))

def myfunc4(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")
    else:
        print("I don't like fruits")

myfunc4(fruit='pineapple')
myfunc4()

# *args and **kwargs combined
def myfunc5(*args,**kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs["fruit"]}")
        print(f"May I have some {kwargs["juice"]} juice?")
    else:
        pass
myfunc5('eggs','spam',fruit="cherries",juice="orange")