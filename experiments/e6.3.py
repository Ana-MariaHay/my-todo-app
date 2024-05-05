file_list = ["a.txt", "b.txt", "c.txt"]
for filename in file_list:
    file = open(f"../files/{filename}", 'r')
    text = file.read()
    print(text)
    file.close()