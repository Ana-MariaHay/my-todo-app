def get_max():
    grades = [9.6, 9.2, 9.7]
    grades.sort()
    return grades[-1]


high_grade = get_max()
print(high_grade)