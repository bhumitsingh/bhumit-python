"""
Python's Standard Library is a vast collection of modules that provides a wide range of functionality out of the box.
"""
import array
import math
import random

arr=array.array('i',[1,2,3,4,5])
print(arr)  # array('i', [1, 2, 3, 4, 5])

print(math.pi)  # 3.141592653589793
print(math.sqrt(25))  # 5.0

print(random.randint(1, 100))  # Random number between 1 and 100
print(random.choice(['apple', 'banana', 'cherry']))  # Random

## File and Directory Access - os module is used for file operations. It provides a way to interact with the operating system.

import os
print(os.getcwd())  # Current working directory

#os.mkdir('test')  # Create a directory

## High level file operations - shutil module is used for high level file operations. It is used to copy, move, and remove files and directories.
import shutil
shutil.copy('source.txt', 'destination.txt')  # Copy

## Data Serialization - json module is used for data serialization. It is used to convert Python objects to JSON strings and vice versa.
import json
data = {'name': 'John', 'age': 30}
json_string = json.dumps(data)
print(json_string)  # {"name": "John", "age": 30}
print(type(json_string))  # <class 'str'>

parsed_data=json.loads(json_string)
print(parsed_data)  # {'name': 'John', 'age': 30}
print(type(parsed_data))  # <class 'dict'> 

## csv files - csv module is used to read and write CSV files.

import csv

with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['John', 30])
    writer.writerow(['Doe', 25])

with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

## datetime module - datetime module is used to work with dates and times.

from datetime import datetime, timedelta

now = datetime.now()
print(now)  # 2023-03-01 12:00:00.000
print(now.year)  # 2023
print(now.month)  # 3
print(now.day)  # 1
print(now.hour)  # 12
yesterday = now - timedelta(days=1)
print(yesterday)  # 2023-02-28 12:00

## time module - time module is used to work with time-related functions.
import time

print(time.time())  # 1646155200.0
time.sleep(2)
print(time.time())  # 1646155202.0

## regular expressions - re module is used to work with regular expressions. It provides a way to search, match, and manipulate strings based on patterns.
import re
pattern = r'\d+'  # Match one or more digits
text = "There are 123 apples"
match = re.search(pattern, text)
print(match.group())  # 123

