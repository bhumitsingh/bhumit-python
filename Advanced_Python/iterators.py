"""
Iterators:
    Iterators are fundamental concept in Python for iteratinf over a collection, such as lists, tuples,
    dictionaries, sets, etc. withot needing to access the individual elements directly. They are an essential 
    part of Python's iterable interface.

Key Features of Iterators:
    - Object-Oriented: Iterators are objects that implement the iterator protocol, which consists of two methods:
        - __iter__(): This method returns the iterator object itself and is required for an object to be 
        considered an iterator.
        - __next__(): This method returns the next item from the iterator. When there are no more items, to return, 
        it raises a StopIteration exception.
    - Stateful: Iterators maintain their current state, which allows them to remember the last element returned.
                this means when you call __next__() again, it continues from where it left off.
    - Memory Efficient: Since iterators yield one item at a time, they are more memory efficient htan loading 
                        an entire list into memory at once. This is particularly useful for large datasets.

"""
# Example of using the built-in iter() function to create an iterator from a list

class MyIterator:
    def __init__(self, limit):
        self.limit = limit # limit stores maximum value the iterator will generate
        self.current = 0 # current stores the current value of the iterator and initialized to zero
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# Usage
my_iter = MyIterator(5)
for value in my_iter:
    print(value)  # prints 0, 1, 2, 3,

"""
Difference between Iterators and Loops
    - An iterator is an object that implements the iterator protocol, which consists of the __iter__ and
     __next__ methods. Iterators provide a way to traverse a collection(like lsits, tuples, etc.) one element
     at a tiem without exposing the underlying structure.
    - A loop, on the other hand, is a control structure that allows you to execute a block of code repeatedly
     for a specified number of times or until a certain condition is met.
"""

# Custom Range Iterator

class MyRange():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# Usage
my_range = MyRange(1, 6)
for value in my_range:
    print(value)  # prints 1, 2, 3, 4,


# Reading Large Files

class FileLineIterator:
    def __init__(self, filename):
        self.file = open(filename, 'r')
    def __iter__(self):
        return self
    def __next__(self):
        line = self.file.readline()
        if line:
            return line.strip()
        else:
            self.file.close()
            raise StopIteration

# Usage

try:
    file_iterator = FileLineIterator('testfile.txt')
    for line in file_iterator:
        print(line)  # prints each line in the file, one at a time
except FileNotFoundError:
    print("File was not found")

# Fibonacci Sequence

class Fibonacci():
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
        self.current_index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_index < self.limit:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_index += 1
            return result
        else:
            raise StopIteration

# Usage
for num in Fibonacci(10):
    print(num)  # prints the first 10 numbers in the Fibonacci sequence

# Infinite Iterators

import itertools

natural_numbers = itertools.count()

for number in itertools.islice(natural_numbers, 10):
    print(number)