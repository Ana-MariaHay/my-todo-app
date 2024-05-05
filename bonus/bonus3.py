filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
filenames1 = []
for file_name in filenames:
    file_name = file_name.replace(".", "-", 1)
    print(file_name)
    filenames1.append(file_name)

print(filenames)
print(filenames1)

