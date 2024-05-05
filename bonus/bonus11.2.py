def get_average():
    with open('../files/data.txt', 'r') as file:
        data = file.readlines()

    temps = data[1:]
    temps = [float(i) for i in temps]

    average = sum(temps) / len(temps)
    return average


new_ave = get_average()
print("average " + str(new_ave))