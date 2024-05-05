# file path must exist when one opens the file in read mode
with open("../files/doc.txt", 'r') as file: # mode of open is by default read, write must have 'w'
    content = file.read()
    print(content)
    