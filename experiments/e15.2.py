import csv

with open("../files/weather.csv", 'r') as file:
    data = list(csv.reader(file))
    print(data)

    city = input("enter a city: ")

    for row in data[1:]:  # skip first line
        if row[0] == city:
            print(row[1])