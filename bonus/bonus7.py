filenames = ["1.doc", "1.report", "1.presentation"]
print(filenames)

new_filenames = [f"{filename.replace('.', '-')}.txt" for filename in filenames]
print(new_filenames)