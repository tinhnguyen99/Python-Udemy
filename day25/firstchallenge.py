# Tinh Nguyen <tinh.nguyentrung1999@gmail.com>

import pandas

data = pandas.read_csv("weather_data.csv")

# Find maximum temperature
temps = data["temp"].to_list()

max_temp = -271
for i in temps:
    if max_temp < i:
        max_temp = i

print(data[data["temp"] == max_temp])

# Use pandas method

max_temp = data.temp.max()

print(max_temp)
print(data[data["temp"] == max_temp])

# create data frame

studens = {
    "name": ["tinh1", "tinh2", "tinh3"],
    "core": [50, 70, 100]
}


new_data = pandas.DataFrame(studens)

new_data.to_csv("studens.csv")

print(new_data)
