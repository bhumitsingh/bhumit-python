'''
What are Exceptions?
Exceptions are events that disrupt thr normal flow of the program. They occur when an error is encountered during
program execution. Common exception include:
    -ZeroDivisionError: Dividing by zero
    -FileNotFoundError: Trying to access a file that does not exist
    -TypeError: Mismatch of data types
    -ValueError: Invalid input value
'''
# Exception try-except block
try:
    # Code that may raise an exception
    x = 10 / 0
except ZeroDivisionError as ex:
    # Code to handle the exception
    print(f"An error occurred: {ex}")
    print("Division by zero is not allowed")

    
try:
    a=b
except NameError as ex:
    print("exception is: ", ex)

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError as ex:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError as ex:
    print("Division by zero is not allowed.")

## try,except,else block

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError as ex:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError as ex:
    print("Division by zero is not allowed.")
except Exception as ex:
    print("An error occurred:", ex)
else:
    print("Division is successful. Result:", result)

## try,except,else,finally block

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError as ex:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError as ex:
    print("Division by zero is not allowed.")
except Exception as ex:
    print("An error occurred:", ex)
else:
    print("Division is successful. Result:", result)
finally:
    print("Execution completed")

### File Handling and Exceptions Handling

try:
    file = open('example1.txt', 'r')
    content = file.read()
    a=b 
    print(content)
except FileNotFoundError as ex:
    print("File not found:", ex)
except Exception as ex:
    print("An error occurred:", ex)
    
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed")