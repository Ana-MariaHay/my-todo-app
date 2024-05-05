import glob
# glob selects all files in the chosen directory

myfiles = glob.glob("../files/*.txt")

print(myfiles)

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())