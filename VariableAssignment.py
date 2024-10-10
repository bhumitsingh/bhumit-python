'''
Dynamic Typing
    -Python uses dynamic typing, meaning you can reassign variables to different data types. This makes Python very
      flexible in assigning data types; it differs from other languages that are statically typed.
Pros and Cons of Dynamic Typing
    -Pros of Dynamic Typing
        -very easy to work with
        -aster development time
    -Cons of Dynamic Typing
        -may result in unexpected bugs!
        -you need to be aware of type()
'''
my_dogs = 2
print(my_dogs)
my_dogs = ['Sammy','Frankie']
print(my_dogs)
'''
Determining variable type with type()
    -You can check what type of object is assigned to a variable using Python's built-in type() function. Common data 
     types include:
        -int (for integer)
        -float
        -str (for string)
        -list
        -tuple
        -dict (for dictionary)
        -set
        -bool (for Boolean True/False)
'''
print(type(my_dogs))