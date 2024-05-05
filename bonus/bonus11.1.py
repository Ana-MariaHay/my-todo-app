def get_temps():
    with open('../files/data.txt', 'r') as file:
        temps = file.readlines()
        temps.pop(0)
    return temps


new_temps = get_temps()
sum_temps = 0
for item in new_temps:
    sum_temps += int(item)

average = sum_temps / len(new_temps)
print("average " + str(average))