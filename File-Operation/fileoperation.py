### Read a whole file

with open('example.txt','r') as file:
    content = file.read()
    print(content)

### Read a file line by line
with open('example.txt','r') as file:
    for line in file:
        print(line.strip()) # strip() method is used to remove the trailing newline character.

### Write to a file(Overwrite)
with open('example.txt','w') as file:
    file.write('Hello World\n')
    file.write('This is a new line\n')

### Write to a file(Append)
with open('example.txt','a') as file:
    file.write('This is appended line\n')

### Writing to a file using writelines()
lines = ['One Line\n', 'Two Line\n', 'Three Line\n']
with open('example.txt','a') as file:
    file.writelines(lines)

### Binary Files

## Writing to a binary file
data = b'\x00\x01\x02\x03\x04\x05'
with open('example.bin', 'wb') as file:
    file.write(data)

## Reading from a binary file
with open('example.bin', 'rb') as file:
    data = file.read()
    print(data)

## Reading and Writing to a file

with open('example.txt', 'w+') as file:
    file.write("Hello World!\n")
    file.write("This is a new line\n")

    file.seek(0)  # Move the cursor to the beginning of the file

    content = file.read()
    print(content)
