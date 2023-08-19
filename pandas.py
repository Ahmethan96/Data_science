import csv

with open("weather_data.csv") as data_file:
    # print(type(data_file))
    # print(type(data_file.readline()))
    # print((data_file.readline()))
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)
## But what if we have more complex data? Tabular data?

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

## 3 lines vs 7 lines while pandas implemented

