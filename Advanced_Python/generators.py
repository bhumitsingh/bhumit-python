"""
Generators:
    - Generators are a type of iterable, like lists or tuples, but unlike lists, they do not store their 
      contents in memory. Instead, they generate items on-the-fly, which makes them more memory-efficient
      ,especially for large datasets.

Key Charateristics of Generators:
    - Memory Efficient: They yield items one at a time and only when requested, so they consume less memory.
    - Lazy Evaluation: Items are generated only as needed, which can lead to performance improvements.
    - Defined using Functions: Generators are defined using functions with the yield keyword instead of return.
"""

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(5)
for number in counter:
    for number in counter:
        print(number)  # prints numbers from 1 to 5
        