'''
There are several testing frameworks available in Python. Some of the popular ones are:
    - Pylint: This is a library that looks at your code and reports back possible issues.
    - unittest: This is a built-in library that allows you to write test cases for your application and check if you are getting desired outputs
    - doctest: This is a built-in library that allows you to write tests in the docstring of your code.
    - pytest: This is a third-party library that is easy to use and allows you to write simple and scalable tests.
'''
# Using pylint to check for possible errors and styling issues in your code
# Python as a set style convention called PEP 8. Pylint is a tool that checks your code against some of the style conventions in PEP 8.

# You can install pylint using pip install pylint. Then you can run it on your code using pylint

def myfunc():
    first = 1
    second = 2
    print(first)
    print(second)

myfunc()

# Running pylint on the above code will give you a score based on the style conventions in PEP 8. It will also give you suggestions on how to improve your code.

# Using unittest to write test cases for your code
